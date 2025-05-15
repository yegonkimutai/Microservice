import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def print_response(resp):
    try:
        print(resp.status_code, resp.json())
    except Exception as e:
        print(f"Error parsing response: {e}")

def test_node_agent():
    # Test Case 1: Normal lifecycle
    print("\n🔹 Test 1: Normal Start ➝ Status ➝ Stop ➝ Status")
    resp = requests.post(f"{BASE_URL}/node/start")
    print_response(resp)

    time.sleep(2)
    resp = requests.get(f"{BASE_URL}/node/status")
    print_response(resp)

    time.sleep(1)
    resp = requests.post(f"{BASE_URL}/node/stop")
    print_response(resp)

    resp = requests.get(f"{BASE_URL}/node/status")
    print_response(resp)

    # Test Case 2: Start twice
    print("\n🔹 Test 2: Attempt to start twice")
    resp = requests.post(f"{BASE_URL}/node/start")
    print_response(resp)
    time.sleep(1)
    resp = requests.post(f"{BASE_URL}/node/start")
    print_response(resp)

    # Test Case 3: Stop without starting
    print("\n🔹 Test 3: Stop when already stopped")
    resp = requests.post(f"{BASE_URL}/node/stop")
    print_response(resp)

    # Test Case 4: Status check when stopped
    print("\n🔹 Test 4: Status check while node is not running")
    resp = requests.get(f"{BASE_URL}/node/status")
    print_response(resp)

    # Test Case 5: Start → wait → Status (uptime test)
    print("\n🔹 Test 5: Start node and check uptime after 3 seconds")
    resp = requests.post(f"{BASE_URL}/node/start")
    print_response(resp)
    time.sleep(3)
    resp = requests.get(f"{BASE_URL}/node/status")
    print_response(resp)

    # Clean-up
    resp = requests.post(f"{BASE_URL}/node/stop")
    print_response(resp)

    # Test Case 6: Corrupt or missing PID file
    print("\n🔹 Test 6: Delete PID file manually and check status")
    import os
    if os.path.exists("node_pid.txt"):
        os.remove("node_pid.txt")
    resp = requests.get(f"{BASE_URL}/node/status")
    print_response(resp)

if __name__ == "__main__":
    test_node_agent()

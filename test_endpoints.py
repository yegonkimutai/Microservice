import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def print_response(resp):
    try:
        print(resp.status_code, resp.json())
    except Exception as e:
        print(f"Error parsing response: {e}")

def test_node_agent():
    print("\n🔹 POST /node/start")
    resp = requests.post(f"{BASE_URL}/node/start")
    print_response(resp)

    time.sleep(2)

    print("\n🔹 GET /node/status")
    resp = requests.get(f"{BASE_URL}/node/status")
    print_response(resp)

    time.sleep(1)

    print("\n🔹 POST /node/stop")
    resp = requests.post(f"{BASE_URL}/node/stop")
    print_response(resp)

    print("\n🔹 GET /node/status")
    resp = requests.get(f"{BASE_URL}/node/status")
    print_response(resp)

if __name__ == "__main__":
    test_node_agent()

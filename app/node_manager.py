import subprocess
import os
import time
import psutil
import platform

PID_FILE = 'node_pid.txt'

def start_node(config=None):
    if os.path.exists(PID_FILE):
        return {"status": "started"}
     
    env = os.environ.copy()
    if config:
        for k, v in config.items():
            env[str(k).upper()] = str(v)

    if platform.system() == 'Windows':
        proc = subprocess.Popen(['bash', 'scripts/fake_node.sh'], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

    with open(PID_FILE, 'w') as f:
        f.write(str(proc.pid))
    return {'status': 'ACTIVE', 'pid': proc.pid}

def stop_node():
    if not os.path.exists(PID_FILE):
        return {'status': 'stopped'}

    with open(PID_FILE, 'r') as f:
        pid = int(f.read())
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(timeout=5)
        os.remove(PID_FILE)
        return {'status': 'INACTIVE'}
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
        os.remove(PID_FILE)
        return {'status': 'not found or already stopped'}

def node_status():
    if not os.path.exists(PID_FILE):
        return {'status': 'not running'}

    with open(PID_FILE, 'r') as f:
        pid = int(f.read())

    try:
        proc = psutil.Process(pid)
        if proc.is_running():
            uptime = time.time() - proc.create_time()
            return {'status': 'running', 'pid': pid, 'uptime_seconds': int(uptime)}
        else:
            return {'status': 'not running'}
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return {'status': 'not running'}

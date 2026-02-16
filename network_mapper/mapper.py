import socket
import json
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        sock.close()
        return port
    except:
        return None

def scan_host(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(ip, p), ports)
        for result in results:
            if result:
                open_ports.append(result)
    return open_ports

def run_scan(target):
    ports = range(1, 1025)
    open_ports = scan_host(target, ports)

    result = {
        "ip": target,
        "open_ports": open_ports
    }

    with open("targets.json", "w") as f:
        json.dump(result, f, indent=4)

    print(f"[+] Scan complete for {target}")
    print(f"Open ports: {open_ports}")

import socket
import json

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        return banner
    except:
        return None

def run_vuln_scan():
    with open("targets.json") as f:
        data = json.load(f)

    ip = data["ip"]
    results = []

    for port in data["open_ports"]:
        banner = grab_banner(ip, port)
        results.append({
            "port": port,
            "banner": banner
        })

    with open("vuln_report.json", "w") as f:
        json.dump(results, f, indent=4)

    print("[+] Vulnerability scan complete")

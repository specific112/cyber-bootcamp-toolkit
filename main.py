import argparse
from network_mapper.mapper import run_scan
from vuln_scanner.scanner import run_vuln_scan

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target", help="Target IP address")
    parser.add_argument("--scan", action="store_true", help="Run network scan")
    parser.add_argument("--vuln", action="store_true", help="Run vulnerability scan")

    args = parser.parse_args()

    if args.scan and args.target:
        run_scan(args.target)

    if args.vuln:
        run_vuln_scan()

if __name__ == "__main__":
    main()


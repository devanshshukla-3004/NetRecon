#!/usr/bin/env python3
"""NetRecon command-line interface."""
import argparse
from netrecon.reporter import build_report, write_json
from netrecon.scanner import scan_ports
from netrecon.utils import parse_ports, resolve_target

def build_parser():
    parser = argparse.ArgumentParser(description="NetRecon - defensive TCP reconnaissance utility")
    parser.add_argument("--target", required=True, help="Authorized hostname or IP address")
    parser.add_argument("--ports", default="1-1024", help="Ports, e.g. 22,80,443 or 1-1024")
    parser.add_argument("--timeout", type=float, default=0.75, help="TCP timeout in seconds")
    parser.add_argument("--workers", type=int, default=50, help="Maximum concurrent workers")
    parser.add_argument("--no-banner", action="store_true", help="Disable banner collection")
    parser.add_argument("--output", default="reports/scan.json", help="JSON report path")
    return parser

def main():
    args = build_parser().parse_args()
    try:
        ports = parse_ports(args.ports)
        resolved_ip = resolve_target(args.target)
    except (ValueError, OSError) as exc:
        print(f"[!] Input error: {exc}")
        return 2

    print("=" * 54)
    print(" NETRECON v1.0 | Network Reconnaissance Utility")
    print("=" * 54)
    print(f"Target       : {args.target}")
    print(f"Resolved IP  : {resolved_ip}")
    print(f"Ports        : {len(ports)}")
    print("Authorization: Use only on systems you own or are permitted to test.")
    print("-" * 54)

    results = scan_ports(resolved_ip, ports, args.timeout, args.workers, not args.no_banner)
    open_results = [r for r in results if r.state == "open"]

    if open_results:
        print("PORT     STATE     SERVICE       BANNER")
        print("-" * 54)
        for result in open_results:
            banner = result.banner[:45] if result.banner else "-"
            print(f"{result.port:<8} {result.state:<9} {result.service:<13} {banner}")
    else:
        print("No open TCP ports found in the selected range.")

    report = build_report(args.target, resolved_ip, results)
    path = write_json(report, args.output)
    print("-" * 54)
    print(f"Scanned ports: {len(results)} | Open ports: {len(open_results)}")
    print(f"Report saved : {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

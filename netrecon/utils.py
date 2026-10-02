"""Utility helpers for NetRecon."""
import ipaddress
import socket

def resolve_target(target: str) -> str:
    target = target.strip()
    try:
        ipaddress.ip_address(target)
        return target
    except ValueError:
        return socket.gethostbyname(target)

def parse_ports(spec: str) -> list[int]:
    ports: set[int] = set()
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if "-" in item:
            start, end = map(int, item.split("-", 1))
            if start > end:
                raise ValueError(f"Invalid port range: {item}")
            ports.update(range(start, end + 1))
        else:
            ports.add(int(item))
    if not ports or any(p < 1 or p > 65535 for p in ports):
        raise ValueError("Ports must be between 1 and 65535.")
    return sorted(ports)

def service_name(port: int) -> str:
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"

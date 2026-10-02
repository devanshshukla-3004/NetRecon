"""Lightweight host reachability checks."""
import socket

def is_reachable(host: str, timeout: float = 1.0) -> bool:
    for port in (443, 80, 22, 53):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except OSError:
            continue
    return False

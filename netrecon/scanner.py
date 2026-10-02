"""TCP connect scanner used by NetRecon."""
from concurrent.futures import ThreadPoolExecutor, as_completed
import socket
from dataclasses import dataclass, asdict
from .utils import service_name

@dataclass
class ScanResult:
    port: int
    state: str
    service: str
    banner: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

def scan_port(host: str, port: int, timeout: float = 0.75, grab_banner: bool = True) -> ScanResult:
    service = service_name(port)
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            banner = ""
            if grab_banner:
                sock.settimeout(min(timeout, 0.5))
                try:
                    banner = sock.recv(256).decode("utf-8", errors="replace").strip()
                except (socket.timeout, OSError):
                    pass
            return ScanResult(port, "open", service, banner)
    except (socket.timeout, ConnectionRefusedError, OSError):
        return ScanResult(port, "closed", service)

def scan_ports(host: str, ports: list[int], timeout: float = 0.75, workers: int = 50,
               grab_banner: bool = True) -> list[ScanResult]:
    results = []
    with ThreadPoolExecutor(max_workers=max(1, min(workers, len(ports) or 1))) as executor:
        futures = {executor.submit(scan_port, host, port, timeout, grab_banner): port for port in ports}
        for future in as_completed(futures):
            results.append(future.result())
    return sorted(results, key=lambda r: r.port)

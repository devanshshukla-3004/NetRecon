"""JSON reporting for NetRecon scans."""
from datetime import datetime, timezone
import json
from pathlib import Path
from .scanner import ScanResult

def build_report(target: str, resolved_ip: str, results: list[ScanResult]) -> dict:
    open_ports = [r for r in results if r.state == "open"]
    return {
        "tool": "NetRecon",
        "version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target": target,
        "resolved_ip": resolved_ip,
        "summary": {"scanned_ports": len(results), "open_ports": len(open_ports)},
        "results": [r.to_dict() for r in results],
    }

def write_json(report: dict, path: str) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return output

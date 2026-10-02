from netrecon.scanner import ScanResult

def test_scan_result_serialization():
    result = ScanResult(443, "open", "https", "HTTP/1.1")
    assert result.to_dict() == {
        "port": 443, "state": "open", "service": "https", "banner": "HTTP/1.1"
    }

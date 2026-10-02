from netrecon.utils import parse_ports
import pytest

def test_parse_ports():
    assert parse_ports("22,80,443,8000-8002") == [22, 80, 443, 8000, 8001, 8002]

def test_parse_ports_rejects_invalid_range():
    with pytest.raises(ValueError):
        parse_ports("100-10")

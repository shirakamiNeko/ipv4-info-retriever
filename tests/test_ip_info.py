import pytest
from src.ip_info import IPv4Info


def test_valid_ip():
    ip_info = IPv4Info("8.8.8.8")
    assert ip_info.ip == "8.8.8.8"
    assert ip_info.city is not None
    assert ip_info.country is not None


def test_invalid_ip():
    with pytest.raises(Exception):
        IPv4Info("invalid_ip")

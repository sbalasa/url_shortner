import pytest

from shorten_url import get_cached_urls, encode

# Global
ecoded_url = ""


def test_encode():
    global encoded_url
    encoded_url = encode("http://testing.com/url_shortening_test")
    assert 8 == len(encoded_url)


def test_cached_urls():
    assert {f"{encoded_url}": "http://testing.com/url_shortening_test"} == get_cached_urls()

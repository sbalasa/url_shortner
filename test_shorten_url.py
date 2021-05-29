import pytest

from shorten_url import get_cached_urls, encode

# Global
ecoded_url = ""


@pytest.fixture
def long_url():
    return "http://testing.com/url_shortening_test"


def test_encode(long_url):
    global encoded_url
    encoded_url = encode(long_url)
    assert 8 == len(encoded_url)


def test_cached_urls(long_url):
    assert {f"{encoded_url}": long_url} == get_cached_urls()

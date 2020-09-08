import pytest
import requests


def test_url(url, answer):
    make_url = f"https://{url}"
    assert requests.get(make_url).status_code == int(answer)

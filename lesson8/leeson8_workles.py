import pytest
import requests


@pytest.mark.parametrize('num',[1,2,3,4,5,6,9])
def test_get_redirect(num):
    response = requests.get(f'http://httpbin.org/redirect{num}')
    a = response.history
    for resp in a:
        print(resp.status_code, resp.url)
    print(a)
    print(response.status_code)
    print(response.request)

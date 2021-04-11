import requests
from requests.auth import HTTPBasicAuth


def test_auth():
    r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/kzr/123",
                     auth=("kzr", "123"))
    print(r)

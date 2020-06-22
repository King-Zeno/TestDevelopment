import pytest


@pytest.fixture(scope='class', params='123456', autouse=True)
def login(request):
    yield request.param

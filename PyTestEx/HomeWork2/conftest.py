import pytest

from PyTestEx.HomeWork2.test_1 import Calculator


@pytest.fixture(scope='function', autouse=True)
def login():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("计算结束")

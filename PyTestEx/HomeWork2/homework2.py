import pytest
import yaml

with open('datas.yml') as f:
        datas = yaml.safe_load(f)

class TestCal():

        @pytest.mark.parametrize(('a', 'b', 'c'), datas['add'])
        def test_add(self, login, a, b, c):
                print("测试 相加")
                assert c == login.add(a, b)

        @pytest.mark.parametrize(('a', 'b', 'c'), datas['sub'])
        def test_sub(self, login, a, b, c):
                print("测试 相减")
                assert c == login.sub(a, b)

        @pytest.mark.parametrize(('a', 'b', 'c'), datas['div'])
        def test_div(self, login, a, b, c):
                print("测试 相除")
                assert c == login.div(a, b)

        @pytest.mark.parametrize(('a', 'b', 'c'), datas['mul'])
        def test_mul(self, login, a, b, c):
                print("测试 相乘")
                assert c == login.mul(a, b)

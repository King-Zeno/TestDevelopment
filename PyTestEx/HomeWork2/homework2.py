import pytest

from PyTestEx.HomeWork2.test_1 import Calculator


class TestCal():

        @pytest.mark.parametrize('a,b,c', [
                ('a', 1, 'a1'),
                (1, 1, 1),
                (1, 2, 3),
                (10, 20, 30),
                (3, 4, 7),
                (5, 6, 11)
        ])
        def test_add(self, login, a, b, c):
                self.cal = Calculator()
                print("测试 相加")
                assert c == self.cal.add(a, b)

        @pytest.mark.parametrize('a,b,c', [
                ('a', 1, 'a1'),
                (1, 1, 1),
                (1, 2, 3),
                (10, 20, 30),
                (3, 4, 7),
                (5, 6, 11)
        ])
        def test_sub(self, login, a, b, c):
                self.cal = Calculator()
                print("测试 相减")
                assert c == self.cal.sub(a, b)

        @pytest.mark.parametrize('a,b,c', [
                ('a', 1, 'a1'),
                (1, 1, 1),
                (1, 2, 3),
                (10, 20, 30),
                (3, 4, 7),
                (5, 6, 11)
        ])
        def test_div(self, login, a, b, c):
                self.cal = Calculator()
                print("测试 相除")
                assert c == self.cal.div(a, b)

        @pytest.mark.parametrize('a,b,c', [
                ('a', 1, 'a1'),
                (1, 1, 1),
                (1, 2, 3),
                (10, 20, 30),
                (3, 4, 7),
                (5, 6, 11)
        ])
        def test_mul(self, login, a, b, c):
                self.cal = Calculator()
                print("测试 相乘")
                assert c == self.cal.mul(a, b)

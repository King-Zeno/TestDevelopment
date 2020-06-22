import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class ")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")
        self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1, 1, "判断相等")
        self.assertIn('h', 'this')

    @unittest.skipIf(1 + 1 == 2, "跳过")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3, 4, "判断相等")
        # self.assertIn('h', 'this')


class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1 case0")

    def test_demo1_case1(self):
        print("test_demo1 case1")

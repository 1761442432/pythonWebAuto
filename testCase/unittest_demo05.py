
import unittest

class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('-----测试类中只运行一次，在所有测试方法之前运行-----------')
    @classmethod
    def tearDownClass(cls):
        print('-----测试类中只运行一次，在所有测试方法之后运行-----------')

    def test_demo2(self):
        print("测试方法1")

    def test_demo3(self):
        print("测试方法2")
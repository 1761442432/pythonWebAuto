import unittest

version = 20
class TestDemo1(unittest.TestCase):

    @unittest.skip('直接跳过执行这个用例')
    def test_method1(self):
        print('测试用例1-1')

    @unittest.skipIf(version > 19, '版本大于19，测试用例跳过执行')
    def test_method2(self):
        print('测试用例1-2')
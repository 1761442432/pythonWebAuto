# 1、导包
import unittest

# 2、自定义测试类,需要继承unittest模块中的TestCase类即可
class TestDemo(unittest.TestCase):
    # 书写测试方法，测试用例代码，书写要求，测试方法必须test_ 开头
    def test_method1(self):
        print('测试方法1-1')

    def test_method2(self):
        print('测试方法1-2')

# 4、执行测试用例
# 4.1 光标放在类后面执行所有的测试用例
# 4.2 光标放在方法后面执行当前的方法测试用例
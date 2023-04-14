# 1、导包
# 2、实例化（创建对象）套件对象
# 3、使用套件对象添加用例方法
# 4、实例化对象运行
# 5、使用运行对象去执行套件对象

import unittest

from testCase.unittest_demo01 import TestDemo

suite = unittest.TestSuite()

# 将⼀个测试类中的所有⽅法进⾏添加
# 套件对象.addTest(unittest.makeSuite(测试类名))
suite.addTest(unittest.makeSuite(TestDemo))

# 实例化运行对象
runner = unittest.TextTestRunner();
# 使用运行对象去执行套件对象
# 运⾏对象.run(套件对象)
runner.run(suite)
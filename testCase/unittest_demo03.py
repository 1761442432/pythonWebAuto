
"""
TestSuite与TestLoader区别：
共同点：都是测试套件
不同点：实现方式不同
	TestSuite: 要么添加指定的测试类中所有test开头的方法，要么添加指定测试类中指定某个test开头的方法
	TestLoader: 搜索指定目录下指定字母开头的模块文件中以test字母开头的方法并将这些方法添加到测试套件中，最后返回测试套件
"""

# 1. 导包
# 2. 实例化测试加载对象并添加用例 ---> 得到的是 suite 对象
# 3. 实例化 运行对象
# 4. 运行对象执行套件对象

import unittest

# 实例化测试加载对象并添加用例 ---> 得到的是 suite 对象
# unittest.defaultTestLoader.discover('用例所在的路径', '用例的代码文件名')
# 测试路径：相对路径： ./  代表当前文件夹
# 测试文件名：可以使用 * 通配符，可以重复使用
suite = unittest.defaultTestLoader.discover('./', 'un*.py')
runner = unittest.TextTestRunner()
runner.run(suite)
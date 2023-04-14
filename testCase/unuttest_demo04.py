
import unittest

class class_test(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 每个测试方法执行之前执行的函数
        print("初始化函数：每个测试方法执行之前执行的函数")

    def test_demo(self):
        print("测试方法1")

    def test_demo2(self):
        print("测试方法2")

    # 释放
    def tearDown(self):
        # 每个测试方法执行之后执行的函数
        print("每个测试方法执行之后执行的函数")

import unittest

class TestAssertEqual(unittest.TestCase):
    def test_success(self):
        self.assertEqual('两者符合，则断言成功', '两者符合，则断言成功')

    def test_error(self):
        self.assertEqual('断言失败11122', '两者不符合，则断言失败')

    def test_success2(self):
        self.assertIn('包含', '断言中包含某个元素就能断言成功')

    # 验证断言结果是否为真
    def test_True(self):
        self.assertTrue(True)
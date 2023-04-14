
from common.myDriver import Driver
# 导入测试报告包
import allure

class Test_openBaiduCase:

    def test_open_baidu_case(self):
        # 测试步骤描述
        with allure.step("打开浏览器，访问百度"):
            # 打开浏览器
            my_driver = Driver()
            # 对当前屏幕截图，放在当前目录下
            my_driver.driver.get_screenshot_as_file("./a.png")
            # 将 a.png 截图，添加到测试报告中
            allure.attach.file("./a.png", attachment_type=allure.attachment_type.PNG)

        with allure.step("在百度输入框中，输入123并且搜索"):
            my_driver.driver
            # 输入：123
            my_driver.driver.find_element(By.ID, 'kw').send_keys("123")
            # 点击元素
            my_driver.driver.find_element(By.ID, 'su').click()
            # 对当前屏幕截图，放在当前目录下。a.png 和上面重复了，所以会覆盖
            my_driver.driver.get_screenshot_as_file("./a.png")
            # 将 a.png 截图，添加到测试报告中。allure的测试报告会自动重命名，不会覆盖之前的图片
            allure.attach.file("./a.png", attachment_type=allure.attachment_type.PNG)
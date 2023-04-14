from selenium import webdriver
from selenium.webdriver.edge.service import Service
# import 不一定是导入类，也可以是一个变量 env_dict
from config.env import env_dict

class Driver:
    def __init__(self):
        # 创建 WebDriver 对象，指明使用Edge浏览器驱动
        self.driver = webdriver.Edge(service=Service(r'D:\我的学习资料\编程学习\pythonWebAuto\driver\edgedriver_win64\msedgedriver.exe'))

        # 设置隐式等待10秒
        self.driver.implicitly_wait(10)
        # 最大化窗口
        self.driver.maximize_window()
        # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
        self.driver.get(env_dict["dev"])

if __name__ == '__main__':
    # Driver() 类：因为定义了初始化方法__init__，所以调用时默认会运行初始化方法
    Driver()
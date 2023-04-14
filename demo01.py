# 导入selenium包
from selenium import webdriver
# 如果未配置浏览器驱动的环境变量时，需要导入 service
# 注意：配置 浏览器驱动的环境变量，是指 浏览器驱动的目录 放在 path里面
from selenium.webdriver.edge.service import Service

# 创建 WebDriver 对象，指明使用Edge浏览器驱动
# 如果已经配置浏览器驱动，则可以直接    wd = webdriver.Edge()
# 备注：打开Chrome 浏览器，直接将 webdriver.Edge 替换成 webdriver.Chrome
wd = webdriver.Edge(service=Service(r'D:\我的学习资料\编程学习\pythonWebAuto\driver\edgedriver_win64\msedgedriver.exe'))

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
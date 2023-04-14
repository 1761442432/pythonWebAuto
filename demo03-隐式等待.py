# 导入selenium包
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用Edge浏览器驱动
wd = webdriver.Edge(service=Service(r'D:\我的学习资料\编程学习\pythonWebAuto\driver\edgedriver_win64\msedgedriver.exe'))

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.byhy.net/_files/stock1.html')

# 一般写在 查找元素 的前面
wd.implicitly_wait(10)
element = wd.find_element(By.ID, 'kw')
element.send_keys('通讯\n')

# 返回页面 ID为1 的元素
element = wd.find_element(By.ID,'1')

print(element.text)
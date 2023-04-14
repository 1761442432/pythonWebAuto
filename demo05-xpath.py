# 导入selenium包
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用Edge浏览器驱动
wd = webdriver.Edge(service=Service(r'D:\我的学习资料\编程学习\pythonWebAuto\driver\edgedriver_win64\msedgedriver.exe'))

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
# 输入：123
wd.find_element(By.ID, 'kw').send_keys("123")
# 点击元素
wd.find_element(By.ID, 'su').click()
wd.find_element(By.XPATH, '//*[@id="s_tab"]/div/a[4]').click()

time.sleep(10)

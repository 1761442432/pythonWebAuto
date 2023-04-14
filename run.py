# -*-coding=utf-8-*-
import unittest
import os, time
from report import HTMLTestRunner

# 用例路径
case_path = 'D:\我的学习资料\编程学习\pythonWebAuto\testCase'

def AllTest():
    '''获取所有的测试模块'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(case_path),
        pattern='case*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    '''获取当前的时间'''
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

def run():
    fileName = os.path.join('D:\我的学习资料\编程学习\pythonWebAuto\report',
                            getNowTime() + 'report.html')

    fp = open(fileName,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'巡服带教测试环境单元测试报告',
        description=u'注：为减少时间人力成本，提高转测质量，特每次对测试环境待发布的代码会对基础功能模块进行单元测试，进一步的提高测试效率,如下为用例执行结果，请查阅！')

    runner.run(AllTest())

if __name__ == '__main__':
    run()
import unittest
import time
import os
from BeautifulReport import BeautifulReport


def allTests():
    '''获取所有需要执行的测试用例'''
    suite = unittest.defaultTestLoader.discover(start_dir=os.path.join(os.path.dirname(__file__), 'test_case'),
                                                pattern='test*.py',
                                                top_level_dir=None
                                                )
    return suite


def get_now_time():
    '''获取当前时间'''
    return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))


def run():
    filename = os.path.join(os.path.dirname(__file__),
                            'test_report', get_now_time()+'UIReport.html')
    fp = open(filename, 'w')
    result = BeautifulReport(allTests())
    result.report(filename=get_now_time()+'Report', description='UI自动化测试报告', log_path='reports')


if __name__ == '__main__':
    run()

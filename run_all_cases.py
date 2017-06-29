#coding=utf-8

#######################################################
# FileName:run_all_cases.py
# Author:CathyZhang
# Date:2017-6-8
# Function Description:执行用例，生成报告
#######################################################

import unittest
import HTMLTestRunnerCN
import time

testcase_dir = 'C:\\PO\\testcase'


def create_suite():
    # 实例化测试套件
    suite = unittest.TestSuite()

    # 查找目录testcase_dir下以case_nw开头的测试用例文件.py
    discover = unittest.defaultTestLoader.discover(testcase_dir, pattern='case_nw*.py', top_level_dir=None)

    # 将查找到的测试用例添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTest(test_case)

    return suite

now = time.strftime('%Y%m%d%H%M%S')
reportFile = "C:\\PO\\result\\test_report_" + now + ".html"

all_test_cases = create_suite()
fp = file(reportFile, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='UI Automation Test Report', description='niiwoo')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='UI Automation Test Report of NiiWoo', tester='Cathy')

runner.run(all_test_cases)

fp.close()

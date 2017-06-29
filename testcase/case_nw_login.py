#coding=utf-8

#######################################################
# FileName:case_nw_login.py
# Author:CathyZhang
# Date:2017-6-9
# Function Description:
#######################################################

import unittest
from base import InitDriver
from pages import nw_login_page
import HTMLTestRunnerCN
import time
from common import Assertion


class LoginPage(unittest.TestCase):
    u'''Log in Page 测试用例 '''

    @classmethod
    def setUpClass(cls):
        cls.driver = InitDriver.start_driver()
        cls.login_page = nw_login_page.LoginPage(cls.driver)
        cls.login_page.access_from_home()  # 从“首页 - 我要借款”进入登录页面

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.login_page.click_login_never_page_login_loc()     # 点击“亲，需要登录才能访问哦！”页面的登录button

    def tearDown(self):
        self.login_page.click_back_key()     # 点击设备返回键

    # 使用不存在的账号登录，提示'登录失败，用户不存在'
    def test_001_login_user_not_exist(self):
        u'''测试点：使用不存在的账号登录'''

        self.login_page.input_account_psw('18100000000', 'test123')    # 输入账号密码
        self.login_page.click_login_button()   # 点击“登录”
        error_message = self.login_page.get_text_error_message_user_not_exist()   # 获取登录结果提示信息
        self.assertEqual(error_message, '登录失败，用户不存在')    # 断言提示信息内容
        self.login_page.click_error_alert_confirm_loc()     # 点击'登录失败，用户不存在'弹框中的“确定”，关闭弹框

    # 账号密码为空时，点击“登录”，toast提示“请输入账号”
    def test_002_login_without_account_psw(self):
        u'''测试点：未登录时，点击“首页 - 我要借款”，弹出登录切换页面'''

        self.login_page.click_login_button()  # 点击“登录”
        error_msg = self.login_page.get_toast_account()
        # self.assertEqual(self.driver.current_activity, '.ui.activity.login.MyLoginNeverActivity')
        self.assertEqual(error_msg, '请输入账号'.decode('utf-8'))
        # self.Assert.assert_equal('test', '登录失败，用户不存在'.decode('utf-8'))

        # 点击“登录”页面的“注册”，跳转到注册页面
    def test_003_click_IndexGuarantee_without_login(self):
        u'''测试点：点击“登录”页面的“注册”，跳转到注册页面'''

        self.login_page.click_login_register_loc()   # 点击“注册”
        page_title = self.login_page.show_page_title()
        self.assertEqual(page_title, '注册')     # 断言跳转后的页面标题
        self.login_page.click_back_key()     # 点击设备返回键

    # 点击“登录”页面的“忘记密码”，跳转到重置登录密码页面
    def test_004_click_IndexGuideLine_without_login(self):
        u'''测试点：点击“登录”页面的“忘记密码”，跳转到重置登录密码页面'''

        self.login_page.click_forget_psw_loc()    # 点击“忘记密码”
        page_title = self.login_page.show_page_title()
        self.assertEqual(page_title, '重置登录密码')     # 断言跳转后的页面标题
        self.login_page.click_back_key()       # 点击设备返回键


if __name__ == '__main__':
    now = time.strftime('%Y%m%d%H%M%S')
    reportFile = "C:\\PO\\result\\LoginPage" + now + ".html"

    suite = unittest.TestSuite()
    suite.addTest(LoginPage('test_001_login_user_not_exist'))
    suite.addTest(LoginPage('test_002_login_without_account_psw'))
    suite.addTest(LoginPage('test_003_click_IndexGuarantee_without_login'))
    suite.addTest(LoginPage('test_004_click_IndexGuideLine_without_login'))

    # runner = unittest.TextTestRunner()
    fp = file(reportFile, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Result of Log in page')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='Test Result of Log in page', tester='Cathy')
    runner.run(suite)
    fp.close()

#coding=utf-8

#######################################################
# FileName:testcase_signin.py
# Author:CathyZhang
# Date:2017-6-7
# Function Description:
#######################################################

import unittest
from base import InitDriver
from operation import operate_sign_in
import time


class Signin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = InitDriver.start_driver()
        # 声明welcome_page类对象
        # self.welcome_page = page_welcome.WelcomePage(self.driver)
        cls.sign_in_operate = operate_sign_in.SigninOperate(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_001_wrong_email(self):
        # 调用click_create_account_button
        self.sign_in_operate.SigninFlow('sftest@123.com', 'test111')
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()

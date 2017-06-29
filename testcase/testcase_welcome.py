#coding=utf-8

#######################################################
# FileName:testcase_welcome.py
# Author:CathyZhang
# Date:2017-6-5
# Function Description:
#######################################################

import unittest
from base import InitDriver
from pages import page_welcome
import Assert
import time


class Welcome(unittest.TestCase):

    def setUp(self):
        self.driver = InitDriver.start_driver()
        # 声明welcome_page类对象
        self.welcome_page = page_welcome.WelcomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # def test_001_click_create_account_button(self):
    #     # 调用click_create_account_button
    #     self.welcome_page.click_create_account_button()
    #     time.sleep(5)
    #
    # def test_002_click_sign_in_button(self):
    #     # 调用click_sign_in_button
    #     self.welcome_page.click_sign_in_button()
    #     time.sleep(10)

    def test_003_click_LA_link(self):
        self.welcome_page.click_LA_link()
        time.sleep(10)
        assert Assert.currentActivity('com.android.chrome')

    def test_004_click_PN_link(self):
        self.welcome_page.click_PN_link()
        time.sleep(10)
        assert Assert.currentActivity('com.android.chrome')


if __name__ == '__main__':
    unittest.main()

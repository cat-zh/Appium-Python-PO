#coding=utf-8

#######################################################
# FileName:page_welcome.py
# Author:CathyZhang
# Date:2017-6-5
# Function Description: 封装welcome page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from base import *


# 继承Element类
class WelcomePage(BasePage.Element):
    # 定位元素：通过元素属性定位welcome page页面中的元素

    # Sign in button
    sign_in_button = (By.ID, 'onboarding.walkthrough.button.login')

    # Create account button
    create_account_button = (By.ID, 'onboarding.walkthrough.button.signup')

    # Link: License Agreement
    LA_link = (By.XPATH, '//android.view.View[4]')

    # Link: Privacy Notice
    PN_link = (By.XPATH, '//android.view.View[6]')

    # 操作方法

    def click_sign_in_button(self):
        self.click(self.sign_in_button)

    def click_create_account_button(self):
        self.click(self.create_account_button)

    def click_LA_link(self):
        self.click(self.LA_link)

    def click_PN_link(self):
        self.click(self.PN_link)
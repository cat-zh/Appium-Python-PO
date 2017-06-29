#coding=utf-8

#######################################################
# FileName:page_sign_in.py
# Author:CathyZhang
# Date:2017-6-2
# Function Description:
#######################################################

from selenium.webdriver.common.by import By
from base import *
import page_welcome


class SigninPage(BasePage.Element):

    # Email输入框
    # Email_edit_text = (By.XPATH, '//android.view.View/android.widget.EditText[1]')
    Email_edit_text = (By.XPATH, '//android.view.View[1]/android.widget.EditText[1]')

    # PassWord输入框
    # psw_edit_text = (By.XPATH, '//android.view.View[4]/android.view.View/android.widget.EditText[1]')
    psw_edit_text = (By.XPATH, '//android.view.View[1]/android.widget.EditText[2]')

    # Sign in button
    sign_in = (By.XPATH, '//android.view.View[2]/android.widget.Button[1]')

    # 左上角返回键
    back_button = (By.XPATH, '//android.view.View[1]/android.view.View[1]')

    # Link: I forgot my password
    forgot_psw_link = (By.XPATH, '//android.view.View[1]/android.view.View[5]')

    # Have an access code tips
    access_code_tips = (By.XPATH, '//android.view.View[6]/android.widget.Image[1]')

    # Link: Create one
    create_one_link = (By.XPATH, '//android.view.View[3]/android.view.View[2]')

    def input_email(self, text):
        self.send_keys(self.Email_edit_text, text)

    def input_psw(self, text):
        self.send_keys(self.psw_edit_text, text)

    def click_sign_in(self):
        self.click(self.sign_in)

    def click_create_one_link(self):
        self.click(self.create_one_link)


def SigninFlow(driver, email, psw):
    welcome_page = page_welcome.WelcomePage(driver)
    signin_page = SigninPage(driver)

    welcome_page.click_sign_in_button()
    signin_page.input_email(email)
    signin_page.input_psw(psw)
    signin_page.click_sign_in()


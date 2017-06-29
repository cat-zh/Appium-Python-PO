#coding=utf-8

#######################################################
# FileName:nw_login_page.py
# Author:CathyZhang
# Date:2017-6-7
# Function Description: 封装log in page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from base import *
from nw_home_page import MainPage


# 继承Element类
class LoginPage(BasePage.Element):

    # 定位元素：通过元素属性定位log in page页面中的元素

    # 登录页面输入框
    edit_text_loc = (By.ID, 'com.junte.onlinefinance:id/edtRegisterPhone')

    # 登录按钮
    login_button = (By.ID, 'com.junte.onlinefinance:id/btnLoginGo')

    # 忘记密码
    forget_psw_loc = (By.ID, 'com.junte.onlinefinance:id/btnLoginForgetPassword')

    # 注册
    login_register_loc = (By.ID, 'com.junte.onlinefinance:id/btnLoginRegister')

    # 关闭
    close_page_loc = (By.ID, 'com.junte.onlinefinance:id/ivXX')

    # 第三方登录方式 - 团贷网账号
    tuandai_loc = (By.ID, 'com.junte.onlinefinance:id/tuandai')

    # 第三方登录方式 - 微信
    weichatLogin_loc = (By.ID, 'com.junte.onlinefinance:id/weichatLogin')

    # 第三方登录方式 - qq
    qqLogin_loc = (By.ID, 'com.junte.onlinefinance:id/qqLogin')

    # 第三方登录方式 - 微博
    weiboLogin_loc = (By.ID, 'com.junte.onlinefinance:id/weiboLogin')

    # “亲，需要登录才能访问哦！”页面的登录button
    login_never_page_login_loc = (By.ID, 'com.junte.onlinefinance:id/btnLogin')

    # “登录失败，用户不存在”弹框内容
    error_message_user_not_exist_loc = (By.ID, 'com.junte.onlinefinance:id/contentTv')

    # “登录失败，用户不存在”弹框中“确定”
    error_alert_confirm_loc = (By.ID, 'com.junte.onlinefinance:id/cancelBtn')

    # 注册、重置密码页面的页面标题定位，用以验证是否正确跳转到此页面
    page_title_loc = (By.ID, 'com.junte.onlinefinance:id/txtTitle')


    # 操作方法

    # 输入账号、密码
    def input_account_psw(self, account, psw):
        self.send_keys(self.edit_text_loc, 0, account)
        self.send_keys(self.edit_text_loc, 1, psw)

    # 点击“登录”按钮
    def click_login_button(self):
        self.click(self.login_button)

    # 点击“忘记密码”
    def click_forget_psw_loc(self):
        self.click(self.forget_psw_loc)

    # 点击“注册”
    def click_login_register_loc(self):
        self.click(self.login_register_loc)

    # 点击“关闭”
    def click_close_page_loc(self):
        self.click(self.close_page_loc)

    # 点击“使用团贷网账号登录”
    def click_tuandai_loc(self):
        self.click(self.tuandai_loc)

    # 点击“使用微信账号登录”
    def click_weichatLogin_loc(self):
        self.click(self.weichatLogin_loc)

    # 点击“使用qq账号登录”
    def click_qqLogin_loc(self):
        self.click(self.qqLogin_loc)

    # 点击“使用微博账号”登录
    def click_weiboLogin_loc(self):
        self.click(self.weiboLogin_loc)

    # 点击“亲，需要登录才能访问哦！”页面的登录button
    def click_login_never_page_login_loc(self):
        self.click(self.login_never_page_login_loc)

    # 点击“登录失败，用户不存在”弹框中的“确定”
    def click_error_alert_confirm_loc(self):
        self.click(self.error_alert_confirm_loc)

    # 进入“登录”页面入口：首页- 我要借款，
    def access_from_home(self):
        main_page = MainPage(self.driver)
        # 若首页出现六月活动广告弹框时，关闭此弹框
        if main_page.isdisplay_close_advert_loc():
            main_page.click_close_advert_loc()
        # 点击“首页 - 我要借款”，进入登录选择页面
        main_page.click_IndexLend_loc()
        # 点击“登录”，进入登录页面
        # self.click_login_never_page_login_loc()

    # 获取“登录失败，用户不存在”弹框内容
    def get_text_error_message_user_not_exist(self):
        msg = self.find_element(*self.error_message_user_not_exist_loc).text.encode('utf-8')
        print 'Current Error Message: %s' % msg
        self.get_screenshot()
        return msg

    # 获取toast信息，报错
    def get_toast_account(self):
        # mes = '//*[@text="请输入账号"]'
        # self.find_toast(mes)
        self.get_screenshot()
        return 'test'

    # 获取注册、重置密码页面的页面标题，用以验证是否正确跳转到此页面
    def show_page_title(self):
        page_title = self.find_element(*self.page_title_loc).text.encode('utf-8')
        print 'The current page title is: %s' % page_title
        self.get_screenshot()
        return page_title

#coding=utf-8

#######################################################
# FileName:case_nw_home_page.py
# Author:CathyZhang
# Date:2017-6-7
# Function Description:
#######################################################

import unittest
from base import InitDriver
from pages import nw_home_page
import time


class HomePage(unittest.TestCase):
    u'''Home Page 测试用例 '''

    @classmethod
    def setUpClass(cls):
        cls.driver = InitDriver.start_driver()
        cls.main_page = nw_home_page.MainPage(cls.driver)
        # 若首页出现六月活动广告弹框时，关闭此弹框
        if cls.main_page.isdisplay_close_advert_loc():
            cls.main_page.click_close_advert_loc()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        self.main_page.click_back_key()

    # 点击“首页”右上角“公告”
    def test_001_click_notice_loc(self):
        u'''测试点：点击“首页”右上角“公告”，进入公告页面'''
        self.main_page.click_notice_loc()
        page_title = self.main_page.get_page_title()
        self.assertEqual(page_title, '你我公告')    # 断言跳转后的Activity

    # 未登录时，点击“首页 - 我要借款”
    def test_002_click_IndexLend_without_login(self):
        u'''测试点：未登录时，点击“首页 - 我要借款”，弹出登录切换页面'''
        self.main_page.click_IndexLend_loc()
        activity_name = self.main_page.get_current_activity_name()
        self.assertEqual(activity_name, '.ui.activity.login.MyLoginNeverActivity')

    # 未登录时，点击“首页 - 我要担保”
    def test_003_click_IndexGuarantee_without_login(self):
        u'''测试点：未登录时，点击“首页 - 我要担保”，进入担保项目列表页面'''
        self.main_page.click_IndexGuarantee_loc()
        self.main_page.tap_page_title()
        page_title = self.main_page.get_page_title()
        self.assertEqual(page_title, '担保项目')     # 断言跳转后的页面标题

    # 未登录时，点击“首页 - 附近尽调”
    def test_004_click_IndexGuideLine_without_login(self):
        u'''测试点：未登录时，点击“首页 - 附近尽调”，进入尽调项目列表页面'''
        self.main_page.click_IndexGuideLine_loc()
        # self.main_page.tap_page_title()
        page_title = self.main_page.get_page_title()
        self.assertEqual(page_title, '附近尽调')     # 断言跳转后的页面标题

    # 未登录时，点击“首页 - 我要投资”
    def test_005_click_IndexInvest_without_login(self):
        u'''测试点：未登录时，点击“首页 - 我要投资”，进入投资项目列表页面'''
        self.main_page.click_IndexInvest_loc()
        self.main_page.tap_page_title()
        page_title = self.main_page.get_page_title()
        self.assertEqual(page_title, '投资项目')     # 断言跳转后的页面标题

    # 未登录时，点击“首页 - 担保认证”
    def test_006_click_guarantee_without_login(self):
        u'''测试点：未登录时，点击“首页 - 担保认证”，弹出登录切换页面'''
        self.main_page.click_guarantee_loc()
        activity_name = self.main_page.get_current_activity_name()
        self.assertEqual(activity_name, '.ui.activity.login.MyLoginNeverActivity')

    # 未登录时，点击“首页 - 新手课堂”
    def test_007_click_learn_without_login(self):
        u'''测试点：未登录时，点击“首页 - 新手课堂”，进入新手课堂页面'''
        self.main_page.click_learn_loc()
        page_title = self.main_page.get_page_title()
        self.assertEqual(page_title, '新手课堂')

    # 未登录时，点击“首页 - 理财体验标”
    def test_008_click_experience_without_login(self):
        u'''测试点：未登录时，点击“首页 - 理财体验标”，进入理财体验标列表页面'''
        self.main_page.click_experience_loc()
        page_title = self.main_page.get_page_title()
        self.assertEqual(page_title, '理财体验标')

    # 未登录时，点击“首页 - 签到送礼”
    def test_009_click_gift_without_login(self):
        u'''测试点：未登录时，点击“首页 - 签到送礼”，弹出登录切换页面'''
        self.main_page.click_gift_loc()
        activity_name = self.main_page.get_current_activity_name()
        self.assertEqual(activity_name, '.ui.activity.login.MyLoginNeverActivity')

    # 未登录时，点击“首页 - 天秤工具箱”（屏幕较小的手机需要向上滑动屏幕，才能显示此button）
    def test_010_click_partner_without_login(self):
        u'''测试点：未登录时，点击“首页 - 天秤工具箱”，进入对应页面'''
        self.main_page.swipe_up()
        self.main_page.click_partner_loc()
        page_title = self.main_page.get_page_title()
        self.assertEqual(page_title, '天秤工具箱')    # 断言跳转后的页面标题


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(HomePage('test_003_click_IndexGuarantee_without_login'))
    suite.addTest(HomePage('test_010_click_partner_without_login'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

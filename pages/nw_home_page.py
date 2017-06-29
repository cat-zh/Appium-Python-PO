#coding=utf-8

#######################################################
# FileName:page_nw_home_page.py
# Author:CathyZhang
# Date:2017-6-5
# Function Description: 封装welcome page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from base import *


# 继承Element类
class MainPage(BasePage.Element):
    # 定位元素：通过元素属性定位home page页面中的元素

    # 公告
    notice_loc = (By.ID, 'com.junte.onlinefinance:id/niiwogonggao')

    # 担保认证
    guarantee_loc = (By.ID, 'com.junte.onlinefinance:id/iv_guarantee')

    # 新手课堂
    learn_loc = (By.ID, 'com.junte.onlinefinance:id/iv_learn')

    # 理财体验标
    experience_loc = (By.ID, 'com.junte.onlinefinance:id/iv_experience')

    # 签到送礼
    gift_loc = (By.ID, 'com.junte.onlinefinance:id/iv_gift')

    # 我要借款
    IndexLend_loc = (By.ID, 'com.junte.onlinefinance:id/ivIndexLend')

    # 我要担保
    IndexGuarantee_loc = (By.ID, 'com.junte.onlinefinance:id/ivIndexGuarantee')

    # 附近尽调
    IndexGuideLine_loc = (By.ID, 'com.junte.onlinefinance:id/ivIndexGuideLine')

    # 我要投资
    IndexInvest_loc = (By.ID, 'com.junte.onlinefinance:id/ivInvest')

    # 天秤工具箱
    partner_loc = (By.ID, 'com.junte.onlinefinance:id/tv_partner')

    # 底部tab栏，多个元素（首页、消息、发现、我）同一个resource-id值
    tab_item_loc = (By.ID, 'com.junte.onlinefinance:id/tvMainTabItem')

    # 首次启动后，弹出六月活动广告弹框
    advert_loc = (By.ID, 'com.junte.onlinefinance:id/iv_advert')

    # 首次启动后，弹出六月活动广告的关闭控件
    close_advert_loc = (By.ID, 'com.junte.onlinefinance:id/iv_close')

    # 尽调/担保/投资项目列表页面标题，用来验证是否显示的是担保项目列表
    page_title_loc = (By.ID, 'com.junte.onlinefinance:id/txtTitle')

    # 首页标题
    main_page_title_loc = (By.XPATH, '//android.widget.ImageView[1]')

    # 操作方法

    # 点击“公告”
    def click_notice_loc(self):
        self.click(self.notice_loc)

    # 点击“担保认证”
    def click_guarantee_loc(self):
        self.click(self.guarantee_loc)

    # 点击“新手课堂”
    def click_learn_loc(self):
        self.click(self.learn_loc)

    # 点击“理财体验标”
    def click_experience_loc(self):
        self.click(self.experience_loc)

    # 点击“签到送礼”
    def click_gift_loc(self):
        self.click(self.gift_loc)

    # 点击“我要借款”
    def click_IndexLend_loc(self):
        self.click(self.IndexLend_loc)

    # 点击“我要担保”
    def click_IndexGuarantee_loc(self):
        self.click(self.IndexGuarantee_loc)

    # 点击“附近尽调”
    def click_IndexGuideLine_loc(self):
        self.click(self.IndexGuideLine_loc)

    # 点击“我要投资”
    def click_IndexInvest_loc(self):
        self.click(self.IndexInvest_loc)

    # 点击“天秤工具箱”
    def click_partner_loc(self):
        self.click(self.partner_loc)

    # 点击tab栏“首页”
    def click_tab_shouye_loc(self):
        self.clicks(self.tab_item_loc, 0)

    # 点击tab栏“消息”
    def click_tab_message_loc(self):
        self.clicks(self.tab_item_loc, 1)

    # 点击tab栏“发现”
    def click_tab_discovery_loc(self):
        self.clicks(self.tab_item_loc, 2)

    # 点击tab栏“我”
    def click_tab_me_loc(self):
        self.clicks(self.tab_item_loc, 3)

    # 点击六月活动广告弹框
    def click_advert_loc(self):
        self.click(self.advert_loc)

    # 点击六月活动广告弹框上的关闭
    def click_close_advert_loc(self):
        self.click(self.close_advert_loc)

    # 点击页面标题
    def tap_page_title(self):
        self.driver.tap([(720, 150)], )

    # 获取“尽调/担保/投资项目列表”页面的页面标题
    def get_page_title(self):
        page_title = self.find_element(*self.page_title_loc).text.encode('utf-8')
        print 'The current page title is: %s' % page_title
        self.get_screenshot()
        return page_title

    # 获取首页标题
    def get_main_page_title(self):
        page_title = self.find_element(* self.main_page_title_loc).text.encode('utf-8')
        print 'The current page title is: %s' % page_title
        self.get_screenshot()
        return page_title

    # 检查六月获取广告是否弹出
    def isdisplay_close_advert_loc(self):
        return self.is_display(self.close_advert_loc)


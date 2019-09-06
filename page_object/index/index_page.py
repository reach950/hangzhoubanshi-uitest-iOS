#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""主页"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class IndexPage(BasePage):

    # 首页table
    table_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTable')

    # 我要咨询
    wo_yao_zi_xun_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]'
                                                   '/XCUIElementTypeOther[3]')

    # 办事指南
    ban_shi_zhi_nan_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeOther[1]'
                                                     '/XCUIElementTypeOther[4]')

    # 搜索
    search_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND rect.width == 300')

    # 全部应用
    more_app_loc = (MobileBy.ACCESSIBILITY_ID, '全部')

    # 十字展台-我要办理
    wo_yao_ban_li_loc = (MobileBy.ACCESSIBILITY_ID, '我要办理')

    # 十字展台-我要缴费
    wo_yao_jiao_fei_loc = (MobileBy.ACCESSIBILITY_ID, '我要缴费')

    # 十字展台-我要查询
    wo_yao_cha_xun_loc = (MobileBy.ACCESSIBILITY_ID, '我要查询')

    # 十字展台-我要预约
    wo_yao_yu_yue_loc = (MobileBy.ACCESSIBILITY_ID, '我要预约')

    # 杭州资讯标题
    hz_news_title_loc = (MobileBy.ACCESSIBILITY_ID, '杭州资讯')

    # 杭州资讯更多按钮
    hz_news_more_button_loc = (MobileBy.ACCESSIBILITY_ID, '更多>>')

    # 杭州资讯第一条资讯标题
    hz_news_first_news_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]'
                                                              '/XCUIElementTypeStaticText[2]')

    # tabbar-服务
    tabbar_services_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 95`][1]')

    # tabbar-资讯
    tabbar_news_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 95`][2]')

    # tabbar-我的
    tabbar_mine_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`rect.width == 94`][2]')

    # 打开办事指南页面
    def open_handle_affairs_guide_page(self):
        self.tap_element(self.ban_shi_zhi_nan_loc)

    # 打开智能客服页面
    def open_ai_customer_service_page(self):
        self.tap_element(self.wo_yao_zi_xun_loc)

    # 打开搜索页面
    def open_search_page(self):
        self.tap_element(self.search_loc)

    # 打开全部应用
    def open_all_apps_page(self):
        self.tap_element(self.more_app_loc)

    # 打开我要办理页面
    def open_handle_page(self):
        self.tap_element(self.wo_yao_ban_li_loc)

    # 打开我要缴费页面
    def open_pay_page(self):
        self.tap_element(self.wo_yao_jiao_fei_loc)

    # 打开我要查询页面
    def open_query_page(self):
        self.tap_element(self.wo_yao_cha_xun_loc)

    # 打开我要预约页面
    def open_reserve_page(self):
        self.tap_element(self.wo_yao_yu_yue_loc)

    # 滑动首页到底部资讯展台
    def scroll_to_news(self):
        self.scroll(self.table_loc, name=self.hz_news_title_loc[1])

    # 点击杭州资讯更多按钮
    def click_hz_news_more_button(self):
        self.tap_element(self.hz_news_more_button_loc)

    # 获取第一条资讯标题
    def get_first_news_title(self):
        return self.find_element(self.hz_news_first_news_title_loc).get_attribute('name')

    # 打开第一条资讯详情
    def open_first_news_detail(self):
        self.tap_element(self.hz_news_first_news_title_loc)

    # 切换到服务页面
    def switch_to_services_page(self):
        self.tap_element(self.tabbar_services_loc)

    # 切换到资讯页面
    def switch_to_news_page(self):
        self.tap_element(self.tabbar_news_loc)

    # 切换到我的页面
    def switch_to_mine_page(self):
        self.tap_element(self.tabbar_mine_loc)

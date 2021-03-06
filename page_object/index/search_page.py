#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""搜索页"""

__author__ = 'kejie'

import time
from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class SearchPage(BasePage):
    # 搜索输入框
    search_field_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSearchField')

    # 搜索按钮
    search_button_loc = (MobileBy.ACCESSIBILITY_ID, 'Search')

    # 客服按钮
    customer_service_button_loc = (MobileBy.ACCESSIBILITY_ID, 'kefu')

    # 取消搜索
    cancel_search_loc = (MobileBy.ACCESSIBILITY_ID, '取消')

    # 热门搜索
    hot_search_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND (rect.y == 132 OR rect.y == 175)')

    # 最后一条搜索结果
    last_search_result_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell[-1]')

    # 无结果图片
    no_result_image_loc = (MobileBy.ACCESSIBILITY_ID, 'nothing')

    # 无结果文字
    no_result_text_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name BEGINSWITH "抱歉"')

    # 无结果热门事项
    no_result_hot_items_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND rect.width == 345')

    # 输入关键字搜索
    def search(self, text):
        self.send_keys(self.search_field_loc, text)
        self.tap_element(self.search_button_loc)

    # 点击客服按钮
    def click_customer_service_button(self):
        self.tap_element(self.customer_service_button_loc)

    # 取消搜索
    def cancel_search(self):
        self.tap_element(self.cancel_search_loc)

    # 获取热门搜索的所有关键词
    def get_all_hot_search_words(self):
        search_words = []
        eles = self.find_elements(self.hot_search_loc)
        for ele in eles:
            search_words.append(ele.get_attribute('name'))
        return search_words

    # 滑动到最后一条搜索结果
    def scroll_to_last_search_result(self):
        count = 0
        while not self.find_element(self.last_search_result_loc).is_displayed():
            if count >= 5:
                break
            self.swipe('up')
            time.sleep(0.5)
            count += 1

    # 是否显示无结果页
    def is_no_result_page_display(self):
        if self.find_element(self.no_result_image_loc) and self.find_element(self.no_result_text_loc):
            return True
        else:
            return False

    # 获取无结果页的热门事项
    def get_no_result_hot_items(self):
        hot_items = []
        eles = self.find_elements(self.no_result_hot_items_loc)
        for ele in eles:
            hot_items.append(ele.get_attribute('name'))
        return hot_items

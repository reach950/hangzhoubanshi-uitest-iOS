#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""出具社保证明"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy
from page_object.base_page import BasePage


class ProvideSocialInsuranceCertificatePage(BasePage):
    # 页面标题
    page_title_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeOther" AND name == "出具社会保险信息证明"')

    # 页面是否显示
    def is_displayed(self):
        page_title = self.find_element(self.page_title_loc)
        return True if page_title else False
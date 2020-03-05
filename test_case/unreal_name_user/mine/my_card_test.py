#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档注释"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase


class TestMyCardByUnrealNameUser(BaseCase):
    """我的-我的证照-证照列表-未实名用户"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_open_real_name_authentication_page_by_unreal_name(self):
        """未实名，点击进入实名认证页面"""
        alert_message = '该服务需要实名，请您先完成实名认证！'
        self.main_page.switch_to_mine_page()
        self.mine_page.click_my_card()
        self.assertTrue(self.mine_page.is_alert_message_displayed(alert_message))
        self.mine_page.click_alert_button(button_lable='确定')
        self.assertTrue(self.real_name_authentication_page.is_displayed())


if __name__ == '__main__':
    unittest.main()

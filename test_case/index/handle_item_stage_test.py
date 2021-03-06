#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试办件展台"""

__author__ = 'kejie'

import unittest
from test_case.base_case import BaseCase
from test_case.common_test_step.login import login
from test_case.common_test_step.handle_item import get_handle_item


class TestHandleItemStage(BaseCase):
    """首页-办件展台-办件"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_01_check_handle_item_in_index(self):
        """办件成功，首页显示办件信息"""
        item_name = get_handle_item(self.driver)
        self.index_page.scroll_to_handle_item_stage(item_name)
        self.assertTrue(self.index_page.check_element_by_name(item_name))

    @login
    def test_02_click_handle_item_stage_to_open_message_center(self):
        """点击办件展台，跳转到消息中心"""
        item_name = get_handle_item(self.driver)
        self.index_page.scroll_to_handle_item_stage(item_name)
        self.index_page.click_element_by_name(item_name)
        self.assertTrue(self.message_center_page.is_displayed())
        self.assertIn(item_name, self.message_center_page.get_first_message_info())


if __name__ == '__main__':
    unittest.main()

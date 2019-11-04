#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试个人信息"""

__author__ = 'kejie'

import unittest
import time
from datetime import datetime
from test_case.base_case import BaseCase
from config.login_users import login_users
from test_case.common_test_step.login import login

real_name_user = login_users['real_name_user']
phone_number = real_name_user['phone_number']
identity_number = real_name_user['identity_number']
password = real_name_user['password']
authentication_method = real_name_user['authentication_method']
new_password = 'test1234'


class TestBaseInfo(BaseCase):
    """我的-个人信息-基本信息"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login('unreal_name')
    def test_01_unreal_user_info(self):
        """未实名用户，姓名，性别，身份证号显示为空"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        test_name = self.user_info_page.get_name()
        test_gender = self.user_info_page.get_gender()
        test_identity_number = self.user_info_page.get_identity_number()
        self.assertIsNone(test_name)
        self.assertIsNone(test_gender)
        self.assertIsNone(test_identity_number)
        self.user_info_page.click_real_name_authentication()
        self.assertTrue(self.real_name_authentication_page.is_displayed())

    @login
    def test_02_real_user_info(self):
        """非银行卡认证用户，显示姓名，性别，身份证号"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        test_name = self.user_info_page.get_name()
        test_gender = self.user_info_page.get_gender()
        test_phone_number = self.user_info_page.get_phone_number()
        test_identity_number = self.user_info_page.get_identity_number()
        self.assertIsNone(test_name)
        self.assertIsNone(test_gender)
        self.assertEqual('{}*****{}'.format(phone_number[:3], phone_number[-3:]), test_phone_number)
        self.assertEqual('{}*****************{}'.format(identity_number[0], identity_number[-1]),
                         test_identity_number)

    @login
    def test_03_real_user_authentication_method(self):
        """已实名用户可查看实名认证的方式"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.click_real_name_authentication()
        self.assertTrue(self.authentication_method_page.is_displayed())
        self.assertEqual(self.authentication_method_page.get_authentication_method(), authentication_method)


class TestPasswordManage(BaseCase):
    """我的-个人信息-密码管理"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    @login
    def test_modify_password(self):
        """修改登录密码"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.open_password_manage_page()
        self.password_manage_page.modify_password(password, new_password)
        self.login_page.login(phone_number, new_password)
        self.assertTrue(self.mine_page.is_login())
        self.mine_page.click_user_area()
        self.user_info_page.open_password_manage_page()
        self.password_manage_page.modify_password(new_password, password)
        self.login_page.login(phone_number, password)
        self.assertTrue(self.mine_page.is_login())


class TestAddressManage(BaseCase):
    """我的-个人信息-地址管理"""

    def setUp(self):
        super().setUp()
        create_time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        self.create_detail_address = '详细地址_{}'.format(create_time_now)
        self.create_username = 'name_{}'.format(create_time_now)
        self.create_phone_number = '133{}'.format(create_time_now[-8:])

    def tearDown(self):
        super().tearDown()

    @login
    def test_create_modify_delete_address(self):
        """地址的增删改"""
        self.index_page.switch_to_mine_page()
        self.mine_page.click_user_area()
        self.user_info_page.open_address_manage_page()
        self.address_manage_page.click_create_address_button()
        self.update_address_page.update_address(self.create_detail_address, self.create_username,
                                                self.create_phone_number)
        time.sleep(1)
        self.assertEqual(self.create_username, self.address_manage_page.get_last_address_username())
        self.assertEqual('{}*****{}'.format(self.create_phone_number[:3], self.create_phone_number[-3:]),
                         self.address_manage_page.get_last_address_phone_number())
        self.assertIn(self.create_detail_address, self.address_manage_page.get_last_address_detail())


if __name__ == '__main__':
    unittest.main()

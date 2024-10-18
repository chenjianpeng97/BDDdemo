#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: actionwords.py.py
@time: 2024/9/3 0:22
"""
from page import LoginPage


class Actionwords:
    def i_log_in_with_username_and_password(self, username="", password=""):
        login_page = LoginPage(self.context.driver)
        login_page.username_field_send_keys(username)
        login_page.password_field_send_keys(password)
        login_page.password_field_send_keys(Keys.ENTER)


if __name__ == '__main__':
    pass

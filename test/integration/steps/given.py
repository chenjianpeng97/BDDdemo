#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: given.py
@time: 2024/9/2 23:01
"""
from behave import *
@given(r'I log in with "(.*)" and "(.*)" in login page of Login')
def impl(context, username="", password=""):
    context.actionwords.i_log_in_with_username_and_password(username, password)

if __name__ == '__main__':
    pass

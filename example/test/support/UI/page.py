#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: page.py
@time: 2024/9/3 0:16
"""
from page_objects import PageObject, PageElement


class AccountPage(PageObject):
    # 定义页面元素，经销商信息列表中经销商名称list
    dealer_name_list = PageElement(id_='id_dealer_name_li')
    #


if __name__ == '__main__':
    pass

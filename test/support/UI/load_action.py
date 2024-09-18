#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: load_action.py
@time: 2024/9/3 0:16
"""
import importlib


class LoadActions:
    def __init__(self, context):
        self.context = context

    def load_actionwords(self, step):
        """
        加载step文件中的action方法
        :param step:
        :return:
        """
        if "Login" in step.name:
            loginaction = getattr(importlib.import_module("test.integration.actionwords.login_action"), "LoginAction")

            return loginaction(self.context)


if __name__ == '__main__':
    pass

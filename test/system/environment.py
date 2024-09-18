#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: environment.py
@time: 2024/9/2 23:01
"""
from behave import *


def before_all(context):
    print("before_all")


def after_all(context):
    print("after_all")


def before_feature(context, feature):
    print("before_feature")


def after_feature(context, feature):
    print("after_feature")


def before_scenario(context, scenario):
    print("before_scenario")


def after_scenario(context, scenario):
    print("after_scenario")


def before_step(context, step):
    print("before_step")


def after_step(context, step):
    print("after_step")


def before_tag(context, tag):
    print("before_tag")


def after_tag(context, tag):
    print("after_tag")


if __name__ == '__main__':
    pass

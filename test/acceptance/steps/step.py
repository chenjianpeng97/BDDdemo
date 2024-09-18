#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: step.py
@time: 2024/9/3 0:35
"""
from behave import given, when, then


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


# 假设有一个账户管理的类
class Account:
    def __init__(self, cus_name, balance):
        self.balance = balance
        self.cus_name = cus_name

    # 打印account
    def __str__(self):
        return f"{self.cus_name}的账户"

    def adjust_balance(self, account, operation, value, operate_user):
        if operate_user.role != "财务":
            return "系统报错信息显示“权限不足”"
        if operation == "增加":
            self.balance += value
            return f"{account}余额变为{self.balance}"
        elif operation == "减少":
            if value > self.balance:
                return "系统报错信息显示“账户余额最多减少至0”"
            self.balance -= value
            return f"{account}余额变为{self.balance}"

    def put_change_record(self):
        # 增加余额调整记录的方法
        pass


# 初始化实例
user = User(name="钱经理", role="财务")
account = Account(cus_name="健康医疗", balance=500)


@given('以财务角色"{user}"登录系统')
def step_impl(context, user):
    context.user = user


@given('系统中已有一个账户"{account_name}"')
def step_impl(context, account_name):
    # 这里可以根据需要进行扩展
    assert account_name == context.account.cus_name


@given('"{account_name}"账户余额为"{balance}"元')
def step_impl(context, account_name, balance):
    assert context.account.balance == int(balance)


@when('"{role}"对"{account_name}"的账户做{operation}并输入{change_value}')
def step_impl(context, role, account_name, operation, change_value):
    context.result = context.account_manager.adjust_balance(
        account_name, operation, int(change_value)
    )


@then('本次操作{result}')
def step_impl(context, result):
    assert context.result == result


@when('进入经销商账户变动记录页面')
def step_impl(context):
    pass  # 这里可以扩展记录页面的相关代码


@then('变动记录前2条显示')
def step_impl(context):
    history = context.account_manager.get_history()
    expected_values = [tuple(row) for row in context.table]
    for index, record in enumerate(expected_values):
        assert record == history[index]


if __name__ == '__main__':
    pass

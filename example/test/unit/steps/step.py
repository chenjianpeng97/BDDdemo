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
from behave import given, when, then, use_step_matcher


class User:
    def __init__(self, name, role):
        self.name = name  # 用户名
        self.role = role  # 用户角色

    def login(self, name):
        if name == "self.name":
            return {"token": self.role}
        else:
            return "没有此用户"


# 假设有一个账户类
class Account:
    def __init__(self, cus_name, balance):
        self.balance = balance  # 账户余额
        self.cus_name = cus_name  # 经销商名称

    # 打印account
    def __str__(self):
        return f"{self.cus_name}的账户"


# -- 以上可能是系统已有的代码 --#

# 现在实现这调整功能加入账户管理类
class AccountManager:
    def __init__(self, dealer_account: Account, operator: User):
        self.account = dealer_account
        self.operator = operator

    def adjust_balance(self, operation, change_value) -> str:
        if operation == "增加":
            self.account.balance += change_value
        # 减少时最多减少到0
        elif operation == "减少" and self.account.balance - change_value >= 0:
            self.account.balance -= change_value
        else:
            return "账户余额最多减少至0"
        return "操作成功"


use_step_matcher("parse")


@given('以"{role}"角色"{user}"登录系统')
def step_impl(context, role, user):
    # 初始化实例
    # 这里是单元测试，我们测试实现这个调整功能的类，故UnitTest层级中的测试直接实例用户对象就可以了
    context.user = User(name=user, role=role)


@given('系统中已有一个账户"{account_name}"')
def step_impl(context, account_name):
    # 这里可以根据需要进行扩展
    pass


@given('"{account_name}"账户余额为"{balance}"元')
def step_impl(context, account_name, balance):
    context.account = Account(cus_name=account_name, balance=int(balance))


@when('"{user}"对"{account_name}"的账户做{operation}并输入{change_value}')
def step_impl(context, user, account_name, operation, change_value):
    change_value = int(change_value)
    account_manager = AccountManager(
        dealer_account=context.account, operator=context.user
    )
    context.result = account_manager.adjust_balance(operation, change_value)


use_step_matcher("re")


@then(r'.*余额变为(\d+)')
def step_impl(context, excpected_balance):
    assert context.account.balance == int(excpected_balance)


@then(r'.*显示"(\w+)"')
def step_impl(context, warning_message):
    assert context.result == warning_message, \
        f"实际报错信息：{context.result}，期望报错信息：{warning_message}"


use_step_matcher("parse")


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

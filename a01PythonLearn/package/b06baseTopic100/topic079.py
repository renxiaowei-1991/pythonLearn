#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string


def check_password(password: str):
    """
    校验输入的密码是否符合密码设置规则
    1、密码至少包含一个数字
    2、密码至少包含一个大写字母
    3、密码长度至少6位
    :param password:
    :return:
    """
    pass_list = list(password)
    if len(password) < 6:
        print("密码校验不通过，请重新输入(长度至少6位)")
        return False
    # 使用函数式编程的高阶函数filter过滤出满足条件的结果(字符是数字)，结果转list，如果长度为0，说明密码中没有数字，不满足条件
    elif len(list(filter(lambda x: x in string.digits, list(password)))) == 0:
        print("密码校验不通过，请重新输入(至少包含一个数字)")
        return False
    # 使用函数式编程的高阶函数filter过滤出满足条件的结果(字符是大写字母)，结果转list，如果长度为0，说明密码中没有数字，不满足条件
    elif len(list(filter(lambda x: x in string.ascii_uppercase, list(password)))) == 0:
        print("密码校验不通过，请重新输入(至少包含一个大写字母)")
        return False
    else:
        print("密码校验通过")
        return True


print("密码至少包含一个数字")
print("密码至少包含一个大写字母")
print("密码长度至少6位")
rs = False
while not rs:
    rs = check_password(input("请输入密码："))


#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string


def check_password_01(password: str):
    """
    校验输入的密码是否符合密码设置规则
    1、密码至少包含一个数字
    2、密码至少包含一个大写字母
    3、密码长度至少6位
    :param password:
    :return:
    """
    """
    str.isdigit() 判断字符是否是数字
    str.isupper() 判断字符是否是大写字母
    str.islower() 判断字符是否是小写字母
    str.isascii() 判断字符是否是字母
    """
    rs = True
    # 使用string的方法isdigit判断一个字符是否是数字。any()可以判断list的元素是否包含True，有一个True即为True
    if not any([i.isdigit() for i in password]):
        print("* 需要至少一位数字")
        rs = False
    # 使用string的方法isdigit判断一个字符是否是数字。any()可以判断list的元素是否包含True，有一个True即为True
    if not any([i.isupper() for i in password]):
        print("* 需要至少以为大写字母")
        rs = False
    if len(password) < 6:
        print("* 需要至少6位密码")
        rs = False
    if rs:
        print("密码校验通过")
    return rs


print("密码至少包含一个数字")
print("密码至少包含一个大写字母")
print("密码长度至少6位")
rs = False
while not rs:
    rs = check_password_01(input("请输入密码："))


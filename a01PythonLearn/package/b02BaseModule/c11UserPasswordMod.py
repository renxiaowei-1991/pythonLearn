#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import string

import file

"""
存放用户检查相关功能
"""

def check_user_name(user_name):
    """
    检查用户名是否符合要求，如果符合要求，对用户名进行存储
    :param user_name:
    :return:
    """
    user_file = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\p077_users.txt"
    rs: bool = False
    if len(user_name) <= 6:
        print("长度小于6位，请重新输入")
        return rs

    user_list = []
    with open(user_file, "r+", encoding="utf-8") as f:
        try:
            for user in f.readlines():
                # 去除字符串头尾的指定字符串，默认是空格和换行，否则会匹配错误
                user_list.append(user.strip())
        except BaseException as be:
            print(f"异常 {be}")

    print(user_list)
    # 和上面的检测分开是因为如果长度都不够，就不用进行下面的检测了
    if user_name in user_list:
        print("用户名已存在，请重新输入")
        return rs
    else:
        print("用户名检测通过")
        with open(user_file, "a+", encoding="utf-8") as f:
            try:
                f.write("\n" + user_name)
                print("新用户名已保存")
            except BaseException as be:
                print(f"写入异常， {be}")
        return True


def random_get_passwd(passwd_len: int):
    """
    随机密码生成器
    :param passwd_len: 指定随机生成的密码的长度
    :return: 返回字符串密码
    """
    passwd_char = ""
    # 小写字母字符串
    # print(string.ascii_lowercase)
    # 大写字母字符串
    # print(string.ascii_uppercase)
    # 数字字符串
    # print(string.digits)
    # 获取特殊字符字符串
    # print(string.punctuation)

    # 密码基数列表，密码字符选择的基础
    passwd_char = passwd_char + \
                  string.ascii_lowercase + \
                  string.ascii_uppercase + \
                  string.digits + \
                  string.punctuation
    # random.sample: 从字符串中随机选取指定位数的字符的列表
    return "".join(random.sample(passwd_char, passwd_len))


def check_password(password: str):
    """
    校验输入的密码是否符合密码设置规则
    1、密码至少包含一个数字
    2、密码至少包含一个大写字母
    3、密码长度至少6位
    :param password:
    :return:
    """
    """
    string.digits 获取数字字符串
    string.ascii_uppercase 获取大写字母字符串
    string.ascii_lowercase 获取大写字母字符串
    string.ascii_letters 获取小写字母+大写字母字符串
    string.punctuation 获取特殊字符字符串
    """
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
    if len(password) < 6:
        print("密码校验不通过，请重新输入(长度至少6位)")
        return False
    # 使用string的方法isdigit判断一个字符是否是数字。any()可以判断list的元素是否包含True，有一个True即为True
    elif any([i.isdigit() for i in password]):
        print("密码校验不通过，请重新输入(至少包含一个数字)")
        return False
    # 使用string的方法isdigit判断一个字符是否是数字。any()可以判断list的元素是否包含True，有一个True即为True
    elif any([i.isupper() for i in password]):
        print("密码校验不通过，请重新输入(至少包含一个大写字母)")
        return False
    else:
        print("密码校验通过")
        return True


def check_password_02(password: str):
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
    have_num = any([i.isdigit() for i in password])
    have_upper = any([i.isupper() for i in password])
    if len(password) >= 6 and have_num and have_upper:
        print("密码校验通过")
        return True
    else:
        print("密码校验不通过，请重新输入")
        return False


def check_password_03(password: str):
    """
    校验输入的密码是否符合密码设置规则
    1、密码至少包含一个数字
    2、密码至少包含一个大写字母
    3、密码长度至少6位
    注意：
        每次输入，如果不符合条件，需要输出所有不符合的条件提示。
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


# while True:
#     if check_user_name(input("请输入用户名: ")):
#         break
# print(random_get_passwd(20))

# print("密码至少包含一个数字")
# print("密码至少包含一个大写字母")
# print("密码长度是少6位")
# rs = False
# while not rs:
#     # rs = check_password(input("请输入密码："))
#     # rs = check_password_02(input("请输入密码："))
#     rs = check_password_03(input("请输入密码："))
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
import random
import time
import datetime
import calendar


def demo01_hello_world():
    """
    输出Hello,World!
    :return:
    """
    print("Hello,World!")


def demo02_sum():
    """
    对用户输入的两个数值进行求和
    :return:
    """
    num1 = input("输入第一个数值：")
    num2 = input("输入第二个数值：")
    result_num = float(num1) + float(num2)
    print(result_num)
    print("数值 {0} 和数值 {1} 的和是：{2}".format(num1, num2, result_num))
    return


def demo03_sqrt():
    """
    用户输入数值，求平方根
    :return:
    """
    num1 = input("请输入一个数值：")
    result_num = math.sqrt(float(num1))
    print("数值 %s 的平方根是： %f。" % (num1, result_num))
    return


def demo04_rand():
    """
    生成各种类型随机数
    :return:
    """
    print(random.random())
    print(random.choice(range(1, 10, 1)))
    print(random.randrange(15, 20))
    return


def demo05_is_number(var):
    """
    判断输入的参数是不是数值类型
    :param var:
    :return:
    """
    try:
        num = float(var)
        print("{0} 是数值！".format(var))
    except ValueError:
        print("{0} 不是数值！".format(var))
    return


def demo06_odd_or_even(var):
    """
    判断参数是奇数&偶数，如果不是数值，也返回结果
    :param var:
    :return:
    """
    try:
        num = int(var)
        if num % 2 == 0:
            print("{0} 是偶数！".format(var))
        else:
            print("{0} 是奇数！".format(var))
    except ValueError:
        print("{0} 不是数值！".format(var))
    return


def demo07_is_leap_year(var):
    """
    判断参数是否是闰年，如果输入的不是数值，也进行提示。
    闰年判断规则：
    1) 普通年能被4整除且不能被100整除的为闰年。（如2004年就是闰年，1900年不是闰年）
    2) 世纪年能被400整除的是闰年。（如2000年是闰年，1900年不是闰年）
    :param var:
    :return:
    """
    try:
        year = int(var)
        flag = False
        if year % 400 == 0:
            flag = True
        elif year % 100 == 0:
            flag = False
        elif year % 4 == 0:
            flag = True
        else:
            flag = False

        if flag:
            print("{} 是闰年".format(year))
        else:
            print("{} 不是闰年".format(year))
    except ValueError:
        print("{0} 不是数值！".format(var))
    return


def demo08_is_prime(var):
    """
    判断参数是否是质数，如果不是数值，也进行提示。
    质数判断规则：
    除1和本身之外，不能被任何数整除
    :param var:
    :return:
    """
    try:
        num = int(var)
        flag = True
        for n in range(2, num, 1):
            if num % n == 0:
                flag = False
        if flag:
            print("{0} 是质数！".format(var))
        else:
            print("{0} 不是质数！".format(var))
    except ValueError:
        print("{0} 不是数值！".format(var))
    return


def demo09_get_factorial(var):
    """
    求参数的阶乘。如果参数不是数值，也进行提示。
    阶乘的算法：
    1) 负数没有阶乘
    2) 0,1的阶乘都是1
    3) n!=n*(n-1)...2*1
    :param var:
    :return:
    """
    try:
        num = int(var)
        result_num = 1
        if num < 0:
            print("{} 是负数，负数没有阶乘。".format(var))
        elif num <= 1:
            result_num = 1
        else:
            for n in range(1, num + 1, 1):
                result_num *= n
        print("{} 的阶乘是： {}".format(num, result_num))
    except ValueError:
        print("{0} 不是数值！".format(var))
    return


def demo10_get_nult_table():
    """
    输出99乘法表
    每次输出使用空格分割。
    每次输出左对齐，用空格补齐长度到6，方便对齐。
    :return:
    """
    for n in range(10):
        for m in range(1, n + 1, 1):
            print("{}*{}={}".format(n, m, n*m).ljust(6, ' '), end=' ')
        print()
    return


def demo11_get_calendar(year, month):
    """
    获取指定年月的日历
    :param year:
    :param month:
    :return:
    """
    print(calendar.month(int(year), int(month)))
    return


def demo12_date_sub(tx_date, num):
    """
    python实现sql的date_sub函数功能
    :param tx_date:
    :param num:
    :return:
    """
    in_date = time.mktime(time.strptime(tx_date, "%Y-%m-%d"))
    out_date = time.strftime("%Y-%m-%d", time.localtime(in_date - 24 * 60 * 60))
    return out_date

if __name__ == "__main__":
    # demo01_hello_world()
    # demo02_sum()
    # demo03_sqrt()
    # demo04_rand()
    # demo05_is_number('aa')
    # demo06_odd_or_even('12')
    # demo07_is_leap_year(1904)
    # demo08_is_prime(101)
    # demo09_get_factorial(20)
    # demo10_get_nult_table()
    # demo11_get_calendar(2023, 6)
    print(demo12_date_sub("2023-06-22", 1))

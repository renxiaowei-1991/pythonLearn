#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
import datetime
import calendar

print(__name__)
print(__package__)

def date_add(tx_date, tx_num):
    """
    python实现sql的date_add函数功能
    :param tx_date:10位日期
    :param tx_num:日期加减的整数
    :return:返回计算后的10为日期
    """
    # 输入的格式化日期转时间戳(格式化时间->时间元组->时间戳)
    in_date = time.mktime(time.strptime(tx_date, "%Y-%m-%d"))
    # 对时间戳进行计算后转格式化日期(# 时间戳->(计算)->时间元组->格式化时间)
    out_ate = time.strftime("%Y-%m-%d", time.localtime(in_date + tx_num * 24 * 60 * 60))
    return out_ate


def date_sub(tx_date, tx_num):
    """
    python实现sql的date_sub函数功能
    :param tx_date:10位日期
    :param tx_num:日期加减的整数
    :return:返回计算后的10为日期
    """
    # 输入的格式化日期转时间戳(格式化时间->时间元组->时间戳)
    in_date = time.mktime(time.strptime(tx_date, "%Y-%m-%d"))
    # 对时间戳进行计算后转格式化日期(# 时间戳->(计算)->时间元组->格式化时间)
    out_ate = time.strftime("%Y-%m-%d", time.localtime(in_date - tx_num * 24 * 60 * 60))
    return out_ate


def get_month_start(tx_date):
    """
    python实现sql的获取月初日期函数功能
    :param tx_date: 10位日期
    :return: 返回月初日期
    """
    # 拆分输入日期
    in_year, in_month, in_day = str(tx_date).split('-')
    # 日期中的日改为01
    out_year, out_month, out_day = in_year, in_month, "01"
    # 使用-拼接输出结果
    return '-'.join([out_year, out_month, out_day])


def __add_months_init(tx_date, tx_num):
    """
    python实现sql的add_months函数功能
    这里是预计算，后续还需对日期中"日"的部分进行修正
    例如：add_months_init("2020-06-30", -4)，结果是2020-02-30，是错误的，所以需要对日进行修正，修正过程在真正的add_months中进行
    定义为私有成员，避免外部引用，导致计算结果错误
    :param tx_date: 10位日期
    :param tx_num: 月份加减的整数
    :return: 返回计算后的10为日期
    """
    # 输入的格式化日期拆分成年,月,日
    in_year_s, in_month_s, in_day_s = str(tx_date).split('-')
    # 输入时间的年,月,日转数值类型，方便计算
    in_year_i, in_month_i, in_day_i = int(in_year_s), int(in_month_s), int(in_day_s)

    # 计算年
    # 年的变化是输入日期月+变化月数后，减1，对12整除
    out_year = str(in_year_i + (in_month_i + tx_num - 1) // 12)

    # 计算月
    # 对月份计算后进行判断
    if (in_month_i + tx_num) % 12 == 0:
        in_month_i = 12
    else:
        in_month_i = (in_month_i + tx_num) % 12
    # zfill(0)将字符串进行右对其，使用0补齐到2位宽。等价与rjust(2,"0")
    out_month = str(in_month_i).zfill(2)

    # 计算日
    out_day = str(in_day_i)

    # 将计算好的年/月/日,使用-拼接到一起
    return "-".join([out_year, out_month, out_day])


def add_months(tx_date, tx_num):
    """
    对add_months_init的初步计算结果进行修正，add_months_init的结果中"日"的部分是有问题的。
    例如：add_months_init("2020-06-30", -4)，结果是2020-02-30，是错误的，所以需要对日进行修正，修正过程在这里进行
    :param tx_date: 10位日期
    :param tx_num: 月份加减的整数
    :return: 返回计算后的10为日期
    """
    # 利用add_months_init对日期进行初步计算(日的值有问题)
    tx_date_init = __add_months_init(tx_date, tx_num)
    """
    1) 对初步计算的结果月份+1
    2) 对月份+1后的日期取月初
    3) 对下月月初的日期-1
    4) 如果经过这三步计算的结果与add_months_init的初步计算结果一致，说明初步计算结果没问题，否则就是有问题。总之，直接使用重新计算后的结果即可
    """
    out_date = date_sub(get_month_start(__add_months_init(tx_date_init, 1)), 1)
    return out_date


print(date_add("2023-06-21", 10))
print(date_sub("2023-06-21", 10))
print(add_months("2020-06-30", -4))
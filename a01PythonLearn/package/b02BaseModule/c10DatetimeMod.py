#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from typing import List

"""
存放对时间进行处理的功能
"""


def get_all_date(begin_date: str, end_date: str):
    """
    返回两个日期之间所有的日期(闭区间)
    :param begin_date: 开始时间
    :param end_date: 结束时间
    :return: 结果list集合
    """
    date_list: list[str] = []
    if begin_date <= end_date:
        # 开始日期转datetime.date
        begin_date_d = datetime.datetime.strptime(begin_date, "%Y-%m-%d").date()
        # 结束日期转datetime.date
        end_date_d = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        # 获取两个日期时间差(int)
        day = (end_date_d - begin_date_d).days
        # 根据时间差日期循环获取中间的所有日期，添加到list中
        for d in range(day + 1):
            date_list.append((begin_date_d + datetime.timedelta(days=d)).strftime("%Y-%m-%d"))

    return date_list


def get_all_date_while(begin_date: str, end_date: str):
    """
    返回两个日期之间所有的日期(闭区间)
    :param begin_date: 开始时间
    :param end_date: 结束时间
    :return: 结果list集合
    """
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date = (datetime.datetime.strptime(begin_date, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    return date_list


# print(get_all_date("2022-05-12", "2022-05-18"))
# print(get_all_date_while("2022-05-12", "2022-05-18"))

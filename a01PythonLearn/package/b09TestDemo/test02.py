#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from package.b02BaseModule import c06SortMod


def add_num(list_in, num):
    """列表中添加值"""
    list_in.append(num)
    print(f"列表 {list_in} 添加了元素 {num}")
    return True


def get_median(list_in):
    """
    取列表中位数
    如果有奇数个数，则取中位数
    如果有偶数个数，则取中间两位数的平均值
    :param list_in:
    :return:
    """
    rs_median = 0
    c06SortMod.SortClass.upSort(list_in)
    if len(list_in) % 2 == 0:
        rs_median = (list_in[len(list_in) // 2] + list_in[len(list_in) // 2 - 1]) / 2
    else:
        rs_median = list_in[len(list_in) // 2]
    return rs_median


if __name__ == "__main__":
    list_a = []
    add_num(list_a, 5)
    add_num(list_a, 6)
    print(get_median(list_a))
    add_num(list_a, 7)
    print(get_median(list_a))
    add_num(list_a, 8)
    print(get_median(list_a))
    print(list_a)

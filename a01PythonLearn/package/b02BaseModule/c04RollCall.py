#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random as r

"""
功能说明
    随机点名
    参数 名称列表
"""


def rollCall():
    nameList = ["刘德华", "张学友", "黎明", "郭富城", "周杰伦", "小明", "小红"]
    print(r.choice(nameList))

rollCall()
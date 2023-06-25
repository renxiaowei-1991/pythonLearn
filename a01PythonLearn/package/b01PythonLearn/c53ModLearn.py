#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import random

"""

    os模块
        os模块是与操作系统交互的一个接口

        getcwd()
            获取当前工作目录

"""
print("获取os模块的方法")
print(os.__dir__())
print(type(os.__dir__()))
# for str in os.__dir__() :print(str)
print("当前工作目录：", os.getcwd())
print(sys.path)

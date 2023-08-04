#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import re

"""
正则表达式
    正则表达式是一个特殊的字符序列，能方便的检查一个字符串是否与某种模式匹配
    re模块 使Python语音拥有了全部的正则表达式功能
    compile函数 根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换
    re模块 也提供了与这些方法功能完全一致的函数。这些函数使用一个模式字符串做为它们的第一个参数

re模块函数
    re.match(pattern, string, flags=0)
        re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
        参数说明：
            pattern  匹配的正则表达式
            string   要匹配的字符串
            flags    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
        匹配成功返回匹配的对象，否则返回none


"""
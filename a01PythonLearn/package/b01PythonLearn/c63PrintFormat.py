#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from pprint import pprint
from colorama import init, Fore, Back, Style

"""
print格式化
    print输出的时候可以进行各种格式化
    
    end=" " : 指定行结束符，默认\n
    sep="\\" : 指定多个输出对象之间的分隔符，默认空格
    file=sys.stdout : 输出目标，默认控制台。可以指定file，需要提取通过open打开
    flush=False : 是否立即刷新输出缓冲区，默认False
    repeat=n : 重复输出n次
    encoding="gbk" : 控制输出编码格式
    
    str.format()
    f"{}"
    str % ()

    控制输出颜色
        linux/macOS: 直接使用ANSI转义序列
        windows: colorama模块
"""


def scan_file_path(path: str):
    """
    扫描指定路径下的所有文件，列出文件路径
    :param path:
    :return:
    """
    # os.walk(path): 返回(根目录, 子目录, 文件(列表))元组列表
    for src_path, sub_path, files in os.walk(path):
        for file in files:
            # print(src_path, file, sep="\\")
            print(os.path.join(src_path, file))
    return


def scan_file_path_01(path: str):
    """
    扫描指定路径下的所有文件，列出文件路径
    :param path:
    :return:
    """
    # os.walk(path): 返回(根目录, 子目录, 文件(列表))元组列表
    file_path = r"D:\02helloWorld\03Python\a01pythonLearn\file"
    with open(file_path + "\\file10.txt", "w+", encoding="utf-8") as f:
        for src_path, sub_path, filelist in os.walk(path):
            for file in filelist:
                print(src_path, file, sep="\\", file=f)
                # print(src_path, file, sep="\\")
                print(os.path.join(src_path, file))
    return


file_path = r"D:\02helloWorld\03Python\a01pythonLearn\package"
# scan_file_path(file_path)
# print(Fore.RED, "Hello,World!", Style.RESET_ALL)
# print("\033[1;31mHello, World!\033[0m")
scan_file_path_01(file_path)

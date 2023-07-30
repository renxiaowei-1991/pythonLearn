#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import shutil
import sys


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


def scan_file_num(filepath: str):
    """
    统计文件行数
    :param filepath:
    :return:
    """
    with open(filepath, "r+", encoding="utf=8") as f:
        try:
            return len(f.readlines())
        except BaseException as be:
            print(f"异常: {be}")
            return


def scan_python_file(path: str):
    """
    扫描指定路径，查找py文件，并且输出py文件行数
    判断字符串以.py结尾。两种办法：
    1、正则表达式re.search
    2、字符串函数 string.endswith(".py") ： 判断文件后缀
    3、字符串函数 string.startswith("~$") : 判断文件前缀
    :param path:
    :return:
    """
    pattern = re.compile(r"\.py$", flags=0)
    result = []
    for root_path, sub_path, filelist in os.walk(path):
        # 列表推导式，使用if限定推导式结果
        file_py = [file for file in filelist if pattern.search(file) is not None]
        for f in file_py:
            # os.path.join拼接路径
            print(os.path.join(root_path, f), scan_file_num(os.path.join(root_path, f)))
    return


def manager_file(path: str):
    """
    整理指定目录下文件，按文件类型归类
    shutil.move: 移动文件
    os.listdir: 可以列出当前目录下的所有文件
    os.path.splitext: 可以得到文件后后缀名，例如：txt, mp3
    os.mkdir: 可以创建目录
    shutil.move: 可以移动文件
    :param path:
    :return:
    """
    # 判断目录类型文件夹是否存在，不存在的话需要创建
    if not os.path.exists(os.path.join(path, "json")):
        os.mkdir(path + "\\json")
    if not os.path.exists(path + "\\jpg"):
        os.mkdir(path + "\\jpg")
    if not os.path.exists(path + "\\txt"):
        os.mkdir(path + "\\txt")

    # 根据文件类型移动文件，使用shutil.move
    for root_file, sub_file, filelist in os.walk(path):
        try:
            for file in filelist:
                if file.endswith(".json"):
                    print(os.path.join(path, "json"))
                    shutil.move(os.path.join(root_file, file), os.path.join(path, "json"))
                elif file.endswith(".txt"):
                    print(os.path.join(path, "txt"))
                    shutil.move(os.path.join(root_file, file), os.path.join(path, "txt"))
                elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    print(os.path.join(path, "jpg"))
                    shutil.move(os.path.join(root_file, file), os.path.join(path, "jpg"))
                else:
                    pass
        except BaseException as be:
            print(f"异常： {be}")
            continue
    return


def manager_file_01(path: str):
    """
    整理指定目录下文件，按文件类型归类
    shutil.move: 移动文件
    os.listdir: 可以列出当前目录下的所有文件
    os.path.splitext: 可以得到文件后后缀名，例如：txt, mp3
    os.mkdir: 可以创建目录
    shutil.move: 可以移动文件
    string.endswith(".py") ： 字符串函数,判断文件后缀
    string.startswith("~$") : 字符串函数,判断文件前缀
    :param path:
    :return:
    """
    # 判断目录类型文件夹是否存在，不存在的话需要创建
    if not os.path.exists(os.path.join(path, "json")):
        os.mkdir(path + "\\json")
    if not os.path.exists(path + "\\jpg"):
        os.mkdir(path + "\\jpg")
    if not os.path.exists(path + "\\txt"):
        os.mkdir(path + "\\txt")

    # 根据文件类型移动文件，使用shutil.move
    for root_file, sub_file, filelist in os.walk(path):
        try:
            for file in filelist:
                if file.endswith(".json"):
                    print(os.path.join(path, "json"))
                    shutil.move(os.path.join(root_file, file), os.path.join(path, "json"))
                elif file.endswith(".txt"):
                    print(os.path.join(path, "txt"))
                    shutil.move(os.path.join(root_file, file), os.path.join(path, "txt"))
                elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                    print(os.path.join(path, "jpg"))
                    shutil.move(os.path.join(root_file, file), os.path.join(path, "jpg"))
                else:
                    pass
        except BaseException as be:
            print(f"异常： {be}")
            continue
    return


def manager_file_01(path: str):
    """
    整理指定目录下文件，按文件类型归类
    shutil.move: 移动文件
    os.listdir: 可以列出当前目录下的所有文件
    os.path.splitext: 可以得到文件后后缀名，例如：txt, mp3
        返回元组(文件路径, 文件后缀)
    os.mkdir: 可以创建目录
    shutil.move: 可以移动文件
    :param path:
    :return:
    """
    # 判断目录类型文件夹是否存在，不存在的话需要创建
    if not os.path.exists(os.path.join(path, "json")):
        os.mkdir(path + "\\json")
    if not os.path.exists(path + "\\jpg"):
        os.mkdir(path + "\\jpg")
    if not os.path.exists(path + "\\txt"):
        os.mkdir(path + "\\txt")

    # 根据文件类型移动文件，使用shutil.move
    for file in os.listdir(path):
        # print(file)
        try:
            # print(os.path.splitext(file))
            if os.path.splitext(file)[1] == ".json":
                print(os.path.join(path, "json"))
                shutil.move(os.path.join(path, file), os.path.join(path, "json"))
            elif os.path.splitext(file)[1] == ".txt":
                print(os.path.join(path, "txt"))
                shutil.move(os.path.join(path, file), os.path.join(path, "txt"))
            elif os.path.splitext(file)[1] in [".jpg", ".jpeg", ".png"]:
                print(os.path.join(path, "jpg"))
                shutil.move(os.path.join(path, file), os.path.join(path, "jpg"))
            else:
                pass
        except BaseException as be:
            print(f"异常： {be}")
            continue
    return


file_path = r"D:\02helloWorld\03Python\a01pythonLearn\package"
# scan_file_path(file_path)
# scan_file_path_01(file_path)

file_path = r"D:\02helloWorld\03Python\a01pythonLearn\package"
# scan_python_file(file_path)

string = "c01HelloWorld.py"
print(string.endswith(".py"))

file_path = r"D:\02helloWorld\03Python\a01pythonLearn\file"
# manager_file(file_path)
manager_file_01(file_path)
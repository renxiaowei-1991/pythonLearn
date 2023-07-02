#!/usr/bin/env python
# -*- coding:utf-8 -*-

import file
import os
import zipfile
import time


def view_file_path(file_path):
    """
    遍历目录下的所有子目录及文件
    :param file_path:指定遍历的目录
    :return:
    """
    # path = "E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    try:
        for root, dirs, files in os.walk(file_path):
            print('-' * 50 + "根目录" + '-' * 50)
            print(root)
            print('-' * 50 + "目录" + '-' * 50)
            print(dirs)
            print('-' * 50 + "文件" + '-' * 50)
            print(files)
    except Exception as e:
        print(e)
    return


def zip_file_path(src_file_path, zip_file_path):
    """
    压缩文件夹到指定路径&指定名称
    :param src_file_path: 来源文件目录
    :param zip_file_path: 目录文件路径
    :return:
    """
    result = True
    # pathwalk = r"E:\\07-python\\07-projectList\\a01PythonLearn\\walk"
    # pathfile = r"E:\\07-python\\07-projectList\\a01PythonLearn\\file"
    LogTime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))

    if not os.path.exists(zip_file_path):
        os.path.makedirs(zip_file_path)
    os.chdir(zip_file_path)
    print(os.getcwd())
    try:
        with zipfile.ZipFile(LogTime + ".zip", 'w') as zip:
            zip_list = []
            for root, dirs, files in os.walk(src_file_path):
                for file in files:
                    zip_list.append(os.path.join(root, file))
                for dir in dirs:
                    zip_list.append(os.path.join(root, dir))
            for i in zip_list:
                zip.write(i, i.replace(src_file_path, ''))
    except Exception as e:
        print(e)
        result = False

    return result



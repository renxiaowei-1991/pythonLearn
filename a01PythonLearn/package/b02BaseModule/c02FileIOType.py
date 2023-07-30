#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import file


def get_input_file(filepath, filename):
    """
    从标准输入读取内容，存入文件中
    :param filepath:文件存储路径
    :param filename:文件名
    :return:
    """
    # 打开文件，进行读写，如果不存在，创建新文件
    file01 = open(filepath + filename, 'w+')
    # 从标准输入循环读取内容，知道输入的是，结束输入
    print("当前指针位置：", file01.tell())
    in_str = input("请输入内容：")
    while in_str != "end":
        file01.write(in_str + "\n")
        in_str = input()
    # 将缓存区文件写入文件
    file01.flush()
    print("当前指针位置：", file01.tell())
    print("当前操作文件：", file01.name, ",打开模式是：", file01.mode, "，关闭状态是：", file01.closed)
    # 关闭文件
    if not file01.closed:
        file01.close()
    print("当前操作文件：", file01.name, ",打开模式是：", file01.mode, "，关闭状态是：", file01.closed)
    return


def get_file_details(filepath, filename):
    """
    读取指定文件内容
    :param filepath:文件存储路径
    :param filename:文件名
    :return:
    """
    file01 = open(filepath + filename, 'r+')
    print("文件：", filepath + filename, "的内容是：\n")
    for line in file01.readlines():
        print(line, end="")
    if not file01.closed:
        file01.close()
    return


def copy_file_func(srcfile01, srcfile02):
    """
    复制文件，将文件filename01的内容复制到filename02中。
    如果filename01不存在，返回提示结果。
    :param srcfile01:
    :param srcfile02:
    :return:
    """
    if os.path.exists(srcfile01):
        file01 = open(srcfile01, 'r+')
        file02 = open(srcfile02, 'w+')
        for line in file01.readlines():
            file02.write(line)
        if not file01.closed:
            file01.close()
        if not file02.closed:
            file02.close()
    else:
        print("文件：", srcfile01, " 不存在！")
    return


def file_merge_func(srcfile01, srcfile02, tarfile):
    """
    合并文件srcfile01和srcfile02，将结果存入tarfile
    :param srcfile01: 来源文件01
    :param srcfile02: 来源文件02
    :param tarfile: 目标文件
    :return:
    """
    if os.path.exists(srcfile01) and os.path.exists(srcfile02):
        file01 = open(srcfile01, 'r+')
        file02 = open(srcfile02, 'r+')
        file03 = open(tarfile, 'w+')
        for line in file01.readlines():
            file03.write(line)
        for line in file02.readlines():
            file03.write(line)
    elif not os.path.exists(srcfile01):
        print("文件：", srcfile01, " 不存在！")
    else:
        print("文件：", srcfile02, " 不存在！")
    if not file01.closed:
        file01.close()
    if not file02.closed:
        file02.close()
    if not file03.closed:
        file03.close()
    return


def rename_file_func(oldfilename, newfilename):
    """
    修改文件名
    :param oldfilename:
    :param newfilename:
    :return:
    """
    if os.path.exists(oldfilename):
        os.rename(oldfilename, newfilename)
    return


def remove_file_func(filename):
    if os.path.exists(filename):
        os.remove(filename)
    return


def path_change_func(basepath):
    """
    目录创建和目录变更的练习
    :param basepath:
    :return:
    """
    if not os.path.exists(basepath + "\\a01filetest"):
        os.mkdir(basepath + "\\a01filetest")
    print(os.getcwd())
    os.chdir(basepath + "\\a01filetest")
    print(os.getcwd())
    return


def file_join_func():
    """
    实现文件的关联
        可以指定文件，指定管理键
    :return:
    """
    base_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\"

    user_grade = {}
    user_student = {}
    user_list = []
    with open(base_path + "p086_grade.txt", "r+", encoding="utf-8") as fin_grade, \
        open(base_path + "p086_student.txt", "r+", encoding="utf-8") as fin_student, \
        open(base_path + "p086.txt", "w+", encoding="utf-8") as fout:
        try:
            for x in fin_grade.readlines():
                user_id, grade = x.strip().split(",")
                user_grade[user_id] = grade
            for x in fin_student.readlines():
                user_id, user_name = x.strip().split(",")
                user_student[user_id] = user_name
                if user_id in user_grade:
                    user = [user_id, user_name, user_grade[user_id]]
                else:
                    user = [user_id, user_name, "未匹配到成绩"]
                user_list.append(user)
            for user in user_list:
                user.append("\n")
                fout.write(",".join(user))

        except BaseException as be:
            print(f"异常: {be}")

        print(user_grade)
        print(user_student)
        print(user_list)
        return


# 文件存储根目录
base_path = "/file\\"
# get_input_file(base_path, "inputFile.txt")
# get_file_details(base_path, "inputFile.txt")
# copy_file_func(base_path + "file02.txt", base_path + "file03.txt")
# file_merge_func(base_path + "file02.txt", base_path + "file03.txt", base_path + "file04.txt")
# rename_file_func(base_path + "file04.txt", base_path + "file05.txt")
# copy_file_func(base_path + "file05.txt", base_path + "file04.txt")
# remove_file_func(base_path + "file05.txt")
# path_change_func(base_path)
file_join_func()
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import pandas
import numpy

"""
python常识

pip安装
    https://www.python100.com/html/51K7GX82OJT2.html
    默认安装到系统的Python环境中。可以通过target指定安装目录
    安装到指定目录
        pip install pandas --target=D:\02helloWorld\03Python\a01pythonLearn\venv\Lib\site-packages

"""


def pandas_nan_handle_01():
    """
    处理空字符&空字符串&缺失值

    对象复制，重复练习
        注意：不能直接将df赋值给df_a，直接赋值是对象的引用，还是指向同一个对象。使用copy复制出来的就是两个对象了
    :return:
    """
    base_path = r"D:\02helloWorld\03Python\a01pythonLearn\excel"
    # 读取excel数据文件
    df = pandas.read_excel(base_path + "/销售数据.xlsx", sheet_name="Sheet3", usecols=["日期", "销售金额"])

    # 替换空字符
    df["销售金额"] = df["销售金额"].replace(r"\s", "", regex=True)
    # 空字符串替换为NAN
    df["销售金额"] = df["销售金额"].replace("", numpy.NAN)

    # 对象复制，重复练习
    #   注意：不能直接将df赋值给df_a，直接赋值是对象的引用，还是指向同一个对象。使用copy复制出来的就是两个对象了
    df_a = df_b = df_c = df.copy()
    df.fillna(-1, inplace=True)
    print(df)
    print(df_a)
    return


def locals_node():
    """
    locals() 函数会以字典类型返回当前位置的全部局部变量。
    对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
    """
    aa = 111
    bb = 'aaa'
    cc = bb
    return locals()


def popen_node(sql):
    """
    os.popen() 方法用于从一个命令打开一个管道。
    在Unix，Windows中有效
    """
    exe_sql = 'hive -e "{}"'.format(sql)
    print("开始执行：" + exe_sql)
    result = os.popen(exe_sql).readlines()
    return result


def python_node():
    """
    用于记录日常见到的一些方法或模块使用办法
    """
    # locals()使用方法
    print(locals_node())
    sql = ""
    # popen_node(sql)
    return


def test():
    for i in range(20):
        # j = str(i) if i < 10 else i
        j = str("0" + str(i) if i < 10 else i)
        j = str("0" + str(i) if i < 10 else i)
        print("j=",j,",j的类型是:",type(j))

    return

if __name__ == "__main__":
    # python_node()
    # test()
    pandas_nan_handle_01()

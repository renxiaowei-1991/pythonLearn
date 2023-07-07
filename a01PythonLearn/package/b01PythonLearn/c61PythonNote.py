#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


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
    test()
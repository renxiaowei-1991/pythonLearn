#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

"""
Python推导式
    Python推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

推导式种类(Python支持各种数据结构的推导式)
    列表(list)推导式
    字典(dict)推导式
    元组(tuple)推导式
    集合(set)推导式

列表推导式
    格式：
        [表达式 for 变量 in 列表]
        [out_exp_res for out_exp in input_list]
        或者
        [表达式 for 变量 in 列表 if 条件]
        [out_exp_res for out_exp in input_list if condition]
    解释：
        out_exp_res
            列表生成元素表达式，可以是有返回值的函数
        for out_exp in input_list
            迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中
        if condition
            条件语句，可以过滤列表中不符合条件的值
    类似
        for 变量 in 列表:
            if 条件:
                表达式
        将返回的所有值再整合成列表

字典推导式
    格式：
        {key_expr: value_expr for value in collection}
        或
        {key_expr: value_expr for value in collection if condtion}
"""

""""
列表推导式练习
"""


def listDerivation():
    list = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
    print("原始字符串列表：", list)
    print("过滤掉长度小于&等于3的字符串，并且转大写。")
    listRes = [name.upper() for name in list if len(name) > 3]
    print("处理后字符串列表：", listRes)

    print("计算30以内可以被3整除的整数")
    numRes = [num for num in range(1, 30, 1) if num % 3 == 0]
    print("结果：", numRes)


"""
字典推导式练习
    c.items() 
        返回的结果中，每一组是一个元组。这个元组包括两个值。第一个是原来的key，另外一个是value
        可以使用元组存放。也可以直接赋值给两个变量
"""
def dictDerivation():
    c = {"a": 1, "b": 2, "c": 3}
    # 字典推导式
    b = {x[0]: x[1] for x in c.items() if x[1] <= 1}
    # {'a': 1}
    print(b)

    # 字典推导式
    x = {"a": 1, "b": 2, "c": 3}
    y = {key: value for key, value in c.items() if value <= 1}
    # {'a': 1}
    print(y)

    # 字典推导式
    # 字典可以直接被替换
    x = {"a": 1, "b": 2, "c": 3}
    x = {key: value for key, value in c.items() if value <= 1}
    # {'a': 1}
    print(x)
    return


if __name__ == "__main__":
    print("列表推导式练习：")
    listDerivation()
    print("字典推导式练习：")
    dictDerivation()
    
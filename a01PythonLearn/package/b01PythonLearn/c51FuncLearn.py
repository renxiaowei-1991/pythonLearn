#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import math

"""
函数
    内置的方法是函数，各种各样的函数

方法
    模块或者class里面定义的方法才是方法
"""

"""
    基础语句
        del  删除

"""

"""
    type(variable)  
        返回输入的变量类型，如果变量是字典就返回字典类型

"""

"""
    range()
        range函数可以创建一个整数列表，一般用在for循环中
        python3 range() 返回的是一个可迭代对象(类型是对象)，而不是列表类型
        python3 list() 是对象迭代器，可以把range()返回的可迭代对象转为一个列表

    range(stop)
    range(start, stop[, setp])
        start 计数从start开始。默认是从0开始。例如：range(5)等价于range(0, 5)
        stop  计数到stop结束，但不包括stop。例如：range(0, 5)是 [0, 1, 2, 3, 4]，没有5
        step  步长，默认为1。例如：range(0, 5)等价于 range(0, 5, 1)
        range(5) 等价于 range(0, 5, 1)
    range([start,]stop[,step])
"""
print("range()函数练习：")
# python3 range() 返回可迭代对象，不是列表
print(range(10))
print(range(0, 10))
print(range(0, 10, 1))
print(range(2, 10, 2))
# python3 list() 是对象迭代器，可以把range()返回的可迭代对象转为一个列表
print(list(range(10)))
print(list(range(0, 10)))
print(list(range(0, 10, 1)))
print(list(range(2, 10, 2)))
print(list(range(5, 5, 1)))

"""
    类型转换
        int(x)
        long(x)
        float(x)
        str(x)   转换为字符串
        repr(x)  转换为表达式字符串
        eval(str) 用来计算在字符串中的有效python表达式，并返回一个对象
        tuple(s)  将序列s转换为一个元组
        list(s)   将序列s转换为一个列表
        chr(x)    将一个整数转换为一个字符
        unichr(x) 将一个整数转换为unicode字符
        hex(x)    将一个整数转换为一个十六进制字符串
        oct(x)    将一个整数转换为一个八进制字符串
"""

"""
    str.format() 格式化函数
        使用 {} 和 : 替换 %
            可以接受不限个数参数，位置可以不按照顺序

            参数可以按照顺序列出，也可以按照顺序按key值字典
            参数支持 列表、元组、字典
            列表和元组 替换的时候，列表和元组 变量名前加一个 *
            字典 替换的时候，字典 变量名前加两个 **
            如果不使用* **，则使用 0[] 的这种格式，也就是列表取值 、元组取值、字典取值的方式 引用

            "{} {}".format("hello","world")
            "{0} {1}".format("hello","world")
            "{1} {0} {1}".format("hello","world")

"""

print("字符串格式化练习：")
print("My name is %s and weight is %d kg!" % ('renxiaowei', 75))

print("格式化函数format练习")
print("{} {}".format("hello", "world"))
print("{0} {1}".format("hello", "world"))
print("{1} {0} {1}".format("hello", "world"))
print("{hello} {world} {hello}".format(hello="hello", world="world"))

print("格式化函数format练习:列表")
list = ["hello", "world"]
print("{1} {0} {1}".format(*list))
print("{0[1]} {0[0]} {0[1]}".format(list))

print("格式化函数format练习:元组")
list = ("hello", "world")
print("{1} {0} {1}".format(*list))
print("{0[1]} {0[0]} {0[1]}".format(list))

print("格式化函数format练习:字典")
dict = {'hello': "hello", 'world': "world"}
print("{hello} {world} {hello}".format(**dict))
print("{0[hello]} {0[world]} {0[hello]}".format(dict))

"""
    string.join(seq)
        字符串连接
        以字符串string将seq中的值按照字符串的格式连接到一起

"""
print("join练习")
listA = ['aaa', '123', 'bbb', '45.3']
print(listA)
print("-".join(listA))

"""
    remove()

"""

"""
    append()

"""
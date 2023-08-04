#!/usr/bin/env python
# coding:utf-8

import os

"""
符号使用
    https://blog.csdn.net/Tiddlik/article/details/120089061

* 星号
    单星号*和双星号**除了作为“乘”和“幂”的数值运算符外，还在列表、元组、字典的操作中有着重要作用
    
作为实参
    单星号*
        列表（list）、元组（tuple）前面加星号*
        列表前面加星号作用是将列表解开（unpacke）成多个独立的参数，传入函数。
            ...format(*lista)
        
        当使用列表和元组作为参数，但是不需要解开列表和元组，而是需要作为一个整体传入的时候，不能加*，否则会报错。
        TypeError: 'int' object is not iterable
        
    双星号**
        字典（dict）前面加两星号**
        字典前面加两个星号，是将字典解开成为独立的元素作为形参。
            ...format(**dicta)
        
        当使用字典作为参数，但是不需要解开字典，而是需要作为一个整体传入的时候，不能加**，否则会报错.
        TypeError: 'int' object is not iterable


作为形参：
    单星号*
        参数名前面加*，表示用来接收全部多余的不固定参数。
        *args
            收集所有的多余参数。
            存放在元组中
            args 是习惯写法
            
            def func(*args):
                print(args, type(args))
    
    双星号**
        参数名前面加**，表示用来接收全部多余的关键字参数
        *kwargs
            接收全部多余的关键字参数
            存放在字典中。
            kwargs 是习惯写法
            
            def func(*args, **kwargs):
                print(args, type(args))
                print(kwargs, type(kwargs))
            
    
"""


def add(a, b):
    return a + b


def func(*args, **kwargs):
    """
    使用*args, **kwargs后不能在添加单独的参数，会有各种问题
    :param args:
    :param kwargs:
    :return:
    """
    # print("name=", name)
    # print("age=", age)
    print("args=", args, ",type(args)=", type(args))
    print("kwargs=", kwargs, ",type(kwargs)=", type(kwargs))
    return


if __name__ == "__main__":
    print("*&**作为实参验证")
    print("*验证")
    data = [7, 8]
    # 这里add函数是对两个元素做计算，所有需要把列表解开成元素
    print(add(*data))

    data = {'a': 7, 'b': 8}
    # 这里add函数是对两个元素做计算，所有需要把列表解开成元素，取字典元素的value
    print(add(**data))

    print("列表&序列&字典：不能解包验证。")
    print("集合操作")
    print("使用元组创建集合")
    dSet = set(("Google", "Runoob", "Taobao"))
    print(dSet)
    print("update：将集合添加到集合中")
    aSet = {1, 3}
    dSet.update({1, 3})
    print("这里不能使用*把set打开，会报错，需要的参数是set整体，而不是set里面的单个元素")
    dSet.update(aSet)
    print(dSet)
    print("update：将两个list添加到集合中")
    lista = [1, 4]
    listb = [4, 6]
    print("这里不能使用*把list打开，会报错，需要的参数是list整体，而不是list里面的单个元素")
    dSet.update([1, 4], [4, 6])
    dSet.update(lista, listb)
    print(dSet)

    print("*&**作为形参验证")
    func("aaa", 111, name="rxw", age=32)

#!/usr/bin/env python
# coding:utf-8

import os

"""
符号使用

* 星号
    单星号*和双星号**除了作为“乘”和“幂”的数值运算符外，还在列表、元组、字典的操作中有着重要作用

单星号*
    列表（list）、元组（tuple）前面加星号*
    列表前面加星号作用是将列表解开（unpacke）成多个独立的参数，传入函数。
    
    当使用列表和元组作为参数，但是不需要解开列表和元组，而是需要作为一个整体传入的时候，不能加*，否则会报错。
    TypeError: 'int' object is not iterable

双星号**
    字典（dict）前面加两星号**
    字典前面加两个星号，是将字典解开成为独立的元素作为形参。
    
    当使用字典作为参数，但是不需要解开字典，而是需要作为一个整体传入的时候，不能加**，否则会报错.
    TypeError: 'int' object is not iterable
    
"""


def add(a, b):
    return a + b


if __name__ == "__main__":
    print("*验证")
    data = [7, 8]
    print(add(*data))

    data = {'a': 7, 'b': 8}
    print(add(**data))


    print("集合操作")
    print("使用元组创建集合")
    dSet = set(("Google", "Runoob", "Taobao"))
    print("add：增加元素")
    dSet.add("Facebook")
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
    print("remove：移除元素，如果不存在，则报错")
    dSet.remove(3)
    print(dSet)
    print("discard：移除元素，如果不存在，不报错")
    dSet.discard(5)
    print(dSet)
    print("pop：随机移除一个元素，并返回被移除的元素")
    dSet.pop()
    print(dSet)
    print("len：集合dSet的元素个数：", len(dSet))
    print("判断在集合中是否存在：", 'Google' in dSet)
    print("clear：清空集合。")
    dSet.clear()
    print(dSet)
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

"""
集合(set）
    集合是一个无序的不重复元素序列。意味着集合不能被索引
    可以使用大括号{}或者set()函数创建集合。
    创建一个空集合必须使用set()而不是{}，因为{}是用来创建空字典的。

    格式：
        parame = {value01,value02,...}
        parame = set(value)

    基本操作：
        s.add(x)     添加元素
        s.update(x)  添加元素，参数可以是列表
        s.remove(x)  移除元素，如果不存在，则报错
        s.discard(x) 移除元素，如果不存在，不报错
        s.pop()      移除元素，随机删除一个元素
        s.clear()    清空集合
        len(x)       集市集合元素个数
        x in s       判断元素是否在集合中存在


"""


def setLearn():
    # 集合：无序&不重复
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    print('orange' in basket)

    print("集合运算")
    aSet = set('abracadabra')
    bSet = set('alacazam')
    print(aSet)
    print(bSet)
    print(aSet - bSet)
    print(aSet | bSet)
    print(aSet & bSet)
    print(aSet ^ bSet)
    cSet = {x for x in aSet if x not in 'abc'}
    print(cSet)

    print("集合操作")
    dSet = set(("Google", "Runoob", "Taobao"))
    print("增加元素")
    dSet.add("Facebook")
    print(dSet)
    dSet.update({1, 3})
    print(dSet)
    dSet.update([1, 4], [4, 6])
    print(dSet)
    print("移除元素")
    dSet.remove(3)
    print(dSet)
    dSet.discard(5)
    print(dSet)
    dSet.pop()
    print(dSet)
    print("集合dSet的元素个数：", len(dSet))
    print("判断在集合中是否存在：", 'Google' in dSet)
    print("清空集合：")
    dSet.clear()
    print(dSet)


if __name__ == "__main__":
    setLearn()
    
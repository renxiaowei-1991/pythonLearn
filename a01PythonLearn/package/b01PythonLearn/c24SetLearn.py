#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

"""
集合(set）
    集合是一个无序的不重复元素序列。意味着集合不能被索引
    集合是无需不重复列表
    可以使用大括号{}或者set()函数创建集合。
    创建一个空集合必须使用set()而不是{}，因为{}是用来创建空字典的。
    使用方法和其它序列的使用类似。不能被索引引用
    
    优点：
        由于存储的方式，检查一个项目是否是一个集合的一部分比检查是不是列表的一部分更快
        
    注意：
        如果添加到集合中的元素有重复值，会自动删除
        通常用集合来消除重复的条目
        集合可以使用数学运算进行组合

    格式：
        parame = {value01,value02,...}
        parame = set(value)

    基本操作：
        s.add(x)     添加元素
            集合添加元素不能使用append
        s.update(x)  添加元素，参数可以是列表
        s.remove(x)  移除特定元素，如果不存在，则报错(经测试，不报错)
        s.discard(x) 移除特定元素，如果不存在，不报错
        s.pop()      移除元素，随机删除一个元素
        s.clear()    清空集合
        len(x)       集市集合元素个数
        x in s       判断元素是否在集合中存在
        
        计算合集：set的方法intersection可以计算两个set的合集
            set01 = set()
            set02 = set()
            set.intersection(set01, set02) # 方法1
            set01.intersection(set02) # 方法2



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
    print("集合推导式。")
    cSet = {x for x in aSet if x not in 'abc'}
    print(cSet)

    print("集合操作")
    print("使用元组创建集合")
    dSet = set(("Google", "Runoob", "Taobao"))
    print("add：增加元素")
    dSet.add("Facebook")
    print(dSet)
    print("update：将集合添加到集合中")
    dSet.update({1, 3})
    print(dSet)
    print("update：将两个list添加到集合中")
    dSet.update([1, 4], [4, 6])
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


if __name__ == "__main__":
    setLearn()

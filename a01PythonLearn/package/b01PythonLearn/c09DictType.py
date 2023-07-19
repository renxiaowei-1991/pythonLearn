#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

"""
    字典
        字典存储键值对
        每个键值 key=>value 对用冒号 : 分割
        每个键值对之间用逗号 , 分割
        整个字典包括在花括号 {} 中
        格式如下：
            d = {key1:value1, key2:value2}

        dict是关键字和内置函数，变量不建议命名dict

    注意
        键一般是唯一的，如果重复，最后一个键值对会替换前面的键值对，值不需要唯一
        值可以是任何数据类型，但键必须是不可改变的，入字符串、数字、元组，但是不能用列表

    修改字典
        dict1 = {'aaa':123,'bbb':'adbd'}
        新增
            dict1['ccc'] = 8
        变更
            dict1['aaa'] = 234
        删除
            del dict1['bbb']  #删除'bbb'
            del dict1         #删除dict1

    函数
        cmp(dict1,dict2)  比较两个字典元素
            Python 3.X 不支持该方法
        len(dict)  计算字典元素个数，键的总数
        str(dict)  输出字典可打印的字符串表示
        type(variable)  返回输入的变量类型，如果变量是字典就返回字典类型

    方法
        dict.clear()
            删除字段内所有元素
        dict.copy()
            返回一个字典的浅复制
        dict.fromkeys(seq[,val])
            创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
        dict.get(key,default=None)
            返回指定键的值，如果值不在字典中返回default值
            dict.get(key, "Not in dictionary") : 如果不在字典中，返回的值可以人为指定。这里既是指定为；Not in dictionary
            样例：
                fib = {1: 1, 2: 1, 3: 2, 4: 3}
                print(fib.get(4, 0) + fib.get(7, 5))
                # 返回 8
        dict.has_key(key)
            如果建在字典dict里返回true，否则返回false 
            Python 3.X 不支持该方法 
        dict.items()
            以列表返回可遍历的(键，值)元组数组
        dict.keys()
            以列表返回一个字典所有的键
        dict.values()
            以列表返回字典中的所有值
        dict.update(dict2)
            把字典dict2的键值对更新到dict里
        pop(key[,default])
            删除字典给定键key所对应的值，返回值为被删除的值。key必须给出，否则返回default值
        popitem()
            返回并删除字典中的最后一对键值对


"""
print("字典练习")
dict1 = {'aaa': 123, 'bbb': 'adbd'}
dict2 = {'aaa': 345, 23.4: 345}
dict3 = {'bbb': ['12', 'aaa', 34.5], 32.4: ('23', 'aaa', 234)}
print(dict1)
print(dict2)
print(dict3)
print("dict1['aaa']:", dict1['aaa'])
print("dict2[23.4]:", dict2[23.4])
print("dict3[32.4]:", dict3[32.4])

print("字典变更")
dict4 = {'aaa': 123, 'bbb': 'adbd'}
dict4['ccc'] = 8
dict4['aaa'] = 234
del dict4['bbb']  # 删除'bbb'
print(dict4)
del dict4  # 删除dict1
# print(dict4)

print("函数&方法练习")
print(dict1.get('bbb'))
print(type(dict1.items()))
print(type(dict1.keys()))
list1 = list(dict1.keys())
print(list1)

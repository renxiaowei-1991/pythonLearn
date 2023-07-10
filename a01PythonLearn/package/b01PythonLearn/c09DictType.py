#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
from pprint import pprint

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
    
    遍历字典
        可以使用dicta.items() + key, value 的形式
    
    注意：
        字典是无需集合
        遍历字典是不能修改字典元素，否则会报错RuntimeError: dictionary changed size during iteration


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



# 字典创建练习
dicta = {}
dicta['a'] = 1
dicta['b'] = 2
print(dicta)


dictc = {"a": 1, "b": 2}
dictc['a'] = 1
dictc['b'] = 2
print(dictc)


dictb = dict()
dictb['a'] = 1
dictb['b'] = 2
print(dictb)

dictd = dict(a=1, b=2)
dictd['a'] = 1
dictd['b'] = 2
print(dictd)




# 遍历字典是不能修改字典元素，否则会报错RuntimeError: dictionary changed size during iteration
d = {"a": 1, "b": 2, "c": 3}

# for mapa in d.keys():
for mapa in list(d.keys()):
    if d[mapa] > 1:
        print(d[mapa])
        d.pop(mapa)
print(d)


# 遍历字典
dicta = {"a": list(range(1, 11)),
         "b": list(range(11, 21)),
         "c": list(range(21, 31))}
pprint(dicta)

for x in dicta.keys():
    print(x + " has value ", dicta[x])

for key, value in dicta.items():
    print(key + " has value ", value)
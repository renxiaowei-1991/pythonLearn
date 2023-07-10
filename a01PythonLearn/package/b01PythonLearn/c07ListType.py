#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
import operator

"""
    列表
        列表的数据项不需要具有相同的类型
        使用方法与字符串索引一样
        列表对 + * 使用方法与字符串类似

    更新列表

    添加元素
        list.appent()

    删除元素
        del list[index]

    列表函数&方法
        函数
        cmp(list1,list2)  比较两个列表的元素
        len(list)         列表元素个数
        max(list)         返回列表元素最大值
        min(list)         返回列表元素最小值
        list(seq)         将元组转换为列表

        方法
        list.append(obj)  在列表末尾添加新的对象
        list.extend(seq)  在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
        list.count(obj)   统计某个元素在列表中出现的次数
        list.index(obj)   从列表中找出某个值第一个匹配项的索引位置
        list.insert(index,obj)  将对象插入列表
        list.pop([index=-1]) 移除列表中的一个元素(默认最后一个元素)，并返回该元素的值
        list.remove(obj)  移除列表中某个值的第一个匹配项
        list.reverse()    反向列表中的元素
        list.sort(cmp=None,key=None,reverse=False)  对原列表进行排序(类型需要相同)

        注意：
            Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象，包含的方法有：
            operator.lt(a, b)
            operator.le(a, b)
            operator.eq(a, b)
            operator.ne(a, b)
            operator.ge(a, b)
            operator.gt(a, b)
            operator.__lt__(a, b)
            operator.__le__(a, b)
            operator.__eq__(a, b)
            operator.__ne__(a, b)
            operator.__ge__(a, b)
            operator.__gt__(a, b)
            
    列表索引
        从前面取：正数(第一个是0)
        从后面取：负数(最后一个是-1)
        
    列表切片
        从前面取：
            a[2:5] (包含a[2]，不包含a[5])
            a[0:3] (前面三个)
            a[:3] (前面三个)
        从后面取：
            a[-3:-1] (后面三个，包含 a[-1])
            a[-3:] (后面三个)
    
    带步长的列表切片
        list[start:end:step]
        样例：
            letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
            letters[0:9:2] 等价与 latters[::2] (从开始到结束，间隔1位取值)
                结果是：['a', 'c', 'e', 'g', 'i']
    
    排序
        listname.sort()
            对listname本身进行排序，返回结果为None。而不是返回一个新list
        listname.sort(reverse=True)
            sort默认是升序排序，添加reverse=True后是降序排序

    获取元素和下标
        enumerate(listname):获取list的元素和下标，返回元组。每个元组包含两个值。元素和index
        listname.index(num):获取num在list中的index

"""
list1 = ['aaa', 'bbb', 123, 23.4]
list2 = [1, 2, 3, 4]
print("list1[0]:", list1[0])
print("list2[1:4]:", list2[1:4])

print("更新列表")
list1[1] = 'ccc'
print("list1:", list1)

print("添加元素")
list2.append('ccc')
print(list2)

print("删除元素")
print("list1:", list1)
del list1[2]
print("list1:", list1)

print("函数&方法练习")
list1 = ['123', 'aaa', 123, 45.6, 'ccc']
list2 = ['123', 'aaa', 123, 45.6, 'ccc']
# list.cmp(list1,list2)
print(operator.eq(list1, list2))
list1.extend(list2)
print(list1)


# enumerate:获取元素和下标(index, item)
a = [1, 2, 3]

for x in a:
    print("Item ", x, " has index ", a.index(x))

for index, item in enumerate(a):
    print("Item ", item, " has index ", index)
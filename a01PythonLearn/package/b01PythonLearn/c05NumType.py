#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math
import cmath
import random

"""
    number类型
        用于存储数值
        数据类型是不允许改变的，如果改变number数据类型的值，将重新分配空间

        整型
        长整型
        浮点型
        复数

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

    del
        删除一些number对象的引用

        del var1[, var2[, var3[...,varN]]]

    math模块、cmath模块
        包括数学运算常用的函数
        math模块 提供了许多对浮点数的数学运算函数
        cmath模块 包含了一下用于复数运算的函数
        cmath模块的函数跟math模块函数基本一致，区别是cmath模块运算的是复数，math模块运算的是数学运算

        import math
            import 导入模块
        dir(math)
            dir 返回模块包含的内容

    数学函数
        abs(x)    绝对值，结果是int
        fabs(x)   绝对值，结果是float
        	已废弃
        ceil(x)   向上取整
        floor(x)  向下取整
        map(x,y)  比较大小，如果x<y 返回-1，如果x==y 返回0，如果x>y 返回1
        max(x1,x2,...)  最大值，参数可以是列表
        min(x1,x2,...)  最小值，参数可以是列表
        round(x[,n])    四舍五入，如果限定，n标识小数点后位数
        sqrt(x)   平方根

    随机数函数
        choice(seq)   从序列中随机选一个元素
            random.choice(range(10)) #从0-9中随机选一个整数
        randrange([start,]stop[,step]) 从指定范围，按指定基数递增的集合随机选一个输
            randrange(0,9,1)
        random()  随机生成下一个实数，范围在[0,1)内
        uniform(x,y) 随机生成下一个实数，范围在[x,y]内
        seed([x]) 改变随机数生成器的种子seed。如果不了解原理，不必特别设定，python会自动设定
        shuffle(lst) 刷新，将序列的所有元素随机排序
            注意：改函数没有返回值

    数学常量
        pi  π
        e   自然常数

"""

# 创建对象
var1 = 1
var2 = 10
print(var1, var2)
# 删除对象引用
del var1, var2
# print(var1, var2)

# 返回模块内容
print("math/cmath模块练习")
print(dir(math))
print(dir(cmath))
print(math.sqrt(4))

print("随机数练习")
list = ['aaa', 'bbb', 123, 344.33, 'dca']
print(random.choice(list))
print(random.randrange(10))
print(round(random.random(), 2))
print(round(random.uniform(1, 10)))
# shuffle() 没有返回值，只是起到一个打乱排序的作用
random.shuffle(list)
print(list)

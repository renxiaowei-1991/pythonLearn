#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    变量类型

    变量存储在内存中的值，这就意味着在创建变量时会在内存中开辟一个空间。
    基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
    因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。
"""

"""
    变量赋值

    Python 中的变量赋值不需要类型声明。
    每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
    每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
    等号 = 用来给变量赋值。
    等号 = 运算符左边是一个变量名，等号 = 运算符右边是存储在变量中的值
"""
counter = 100  # 整型变量
miles = 1000.0  # 浮点型
name = "Jone"  # 字符串

print(counter, miles, name)

"""
    多个变量赋值

    Python允许你同时为多个变量赋值
"""
print("变量赋值练习：")
a = b = c = 1
print(a, b, c)
a, b, c = 2, 3, "Jone"
print(a, b, c)

"""
    标准数据类型

    Python有五个标准的数据类型：
        Numbers（数字）
            Python支持四种不同的数字类型
                int（有符号整型）
                long（长整型，也可以代表八进制和十六进制）
                    用L结束，也可以使用l结束，但是建议使用L，避免混淆
                    long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。
                float（浮点型）
                complex（复数）
        String（字符串）
            字符串或串(String)是由数字、字母、下划线组成的一串字符
            python的字串列表有2种取值顺序
                从左到右索引默认0开始的，最大范围是字符串长度少1
                从右到左索引默认-1开始的，最大范围是字符串开头

                如果你要实现从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
                [头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。

                python 返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。
        List（列表）
            列表用 [] 标识
            列表中的值切割可以用 [头下标:尾下标] 截取
            从左到右索引默认从0开始，从右到左索引默认-1开始，下标可以为空表示取到头或尾
            + 是列表连接运算符
            * 是重复操作运算符

        Tuple（元组）
            元组 类似列表
            元组 只读列表
            元组用 () 标识，内部元素用逗号隔开。
            元组不能二次赋值,不允许更新，相当于只读列表

        Dictionary（字典）
            字典 键值对集合
            列表是有序的对象集合，字典是无序的对象集合
            列表与字典的区别：字典当中的元素是通过键来存取的，而不是通过偏移存取。
            字典用 {} 标识。字典由索引(key)和它对应的值value组成
            字典相当于一张表，要取什么值需要使用字段名(key)来获取对应的值
"""
varInt = 1
varLong = 1.1
varString = "123456"

print("字符串分割练习：")
print(varString[1], varString[-2])
print(varString[1:-2])  # 索引从1到-2，包含头下表，不包含尾下表

print("列表截取练习：")
varList = ['123', 'abs', '23a']
print(varList[0:2])

print("元组练习：")
tuple = ('runoob', 768, 4.5, 'aa', 299)
tinytuple = (123, 'bb')
print(tuple)
print(tuple[0])
print(tuple[0:3])
print(tinytuple * 2)
print(tuple + tinytuple)

print("字典练习：")
dict = {}
dict['one'] = 'This is one'
dict['2'] = 'This is two'
tinydict = {'name': 'runoob', 'code': 454, 'dept': 'sales'}
print(dict['one'])
print(dict['2'])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

dict = {}
dict["one"] = 123
dict['two'] = "aaa"
dict["""thr"""] = 123.4
print(dict)

"""
    数据类型转换
        数据类型的转换，只需要将数据类型作为函数名即可
        int(x) 将x转换为整数
        str(x) 将x转换为字符串
        repr(x) 将x转换为表达式字符串
        eval(str) 计算在字符串中的有效python表达式，返回一个对象
        tuple(s) 将序列s转换为元组
        list(s) 将序列s转换为列表

"""
stringA = "123"
intA = int(stringA)
print(stringA, intA)

intB = 123
stringB = str(intB)
print(intB, stringB)

arrayA = [123, "aaa", 234.5]
arrayB = list(arrayA)
arrayC = tuple(arrayA)
print(arrayA)
print(arrayB)
print(arrayC)

# 123+456
strA = input()
num = repr(strA)
numA = eval(strA)
"""
    删除对象引用

    可以使用del语句删除一些对象的引用
    可以通过使用del语句删除单个或多个对象的引用
"""
var1 = 1
var2 = 10
del var1, var2

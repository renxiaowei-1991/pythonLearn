#!/use/bin/env python
# -*- coding:utf-8 -8-

import time
import calendar
import datetime

"""
    函数
        函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段

    定义函数
        函数代码已def关键词开头，后接函数标识符名称和圆括号()
        任何出入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数
        函数的第一行语句可以选择性地使用文档字符串，用于存放函数说明
        函数内容以冒号起始，并且缩进
        return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None

        def functionName(parameters):
            "函数_文档字符串"
            function_suite
            return [expression]

    函数调用
        参数值和参数名称是按照函数声明中定义的顺序匹配起来的
        函数定义以后，可以通过另一个函数调用执行，也可以直接从Python提示符执行

    可变(mutable)&不可变(immutable)对象
        不可变对象
            Strings,tuples,numbers
        可变对象
            list,dict

        不可变类型
            变量赋值a=5后再赋值a=10，实际上是新生成一个int值对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a
        可变类型
            变量赋值la=[1,2,3,4]后再赋值la[2]=5，是将list la的第三个值更改，本身la没有动，只是其内部的一部分值被修改了

    参数传递
        python中，类型属于对象，变量没有类型
        a = [1,2,3]
        a = "Runoob"
        上面代码，[1,2,3]是List类型，"Runoob"是String类型，变量a没有类型，变量a仅仅是一个对象的引用(一个指针)，
        可以是List类型对象，也可以指向String类型对象

        不可变类型：值传递
            类似C++的值传递，如 整数、字符串、元组。
            如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
        可变类型：引用传递
            类似C++的引用传递，如列表、字典。
            如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

    参数
        必备参数
            必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
        关键字参数
            函数调用使用关键字参数来确定传入的参数值
            使用关键字参数允许函数调用时参数的顺序与声明时不一致，python解释器能够用参数名匹配参数值
        默认参数
            调用函数时，默认参数的值如果没有传入，则被认为是默认值。
        不定长参数
            可能需要一个函数处理比当初声明时更多的参数。这些参数叫做不定长参数。
            不定长参数声明是不会命名
            加了星号(*)的变量名会存放所有未命名的变量参数，该变量是元组类型

            不定长参数不能与关键字参数一起使用

            def functionname([formal_args,] *var_args_tuple):
                "函数_文档字符串"
                function_suite
                return [repression]

    匿名函数
        python使用lambda来创建匿名函数
        lambda只是一个表达式，函数体比def简单很多
        lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
        lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
        虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率

        语法：
            lambda [arg1 [,arg2,...argn]]:expression

    return语句
        return语句[表达式]退出函数，选择性地向调用方返回一个表达式。
        不带参数值的return语句返回None。

    变量作用域
        一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
        变量的作用域决定了在哪一部分你可以访问哪个特定的变量名称。

        全局变量
            定义在函数外的拥有全局作用域
            全局变量可以在整个程序范围内访问
            调用函数是，所以在函数内声明的变量名称都将被加入到作用域中
        局部变量
            定义在函数内部的变量拥有一个局部作用域
            局部变量只能在其被声明的函数内部访问

"""

print("普通函数练习")


def printme(str):
    print(str)
    return


printme("Hello World!")

# 不可变对象参数
print("不可变对象参数")


def immutableChangeIne(a):
    a = 10


b = 2
immutableChangeIne(b)
print(b)

# 可变对象参数
print("可变对象参数")


def mutableChangeList(myList):
    myList.append([1, 2, 3, 4])
    print("函数内取值", myList)
    return


list1 = [2, 3, 4]
mutableChangeList(list1)
print("函数外取值", list1)

# 关键字参数&默认参数
print("关键字参数&默认参数")


def printinfo(name, ago, sex="male"):
    print("name:", name)
    print("ago:", ago)
    print("sex:", sex)
    return


printinfo(ago=10, name="renxw")

"""
不定长参数
    不定长参数不能与关键字参数一起使用
    加了星号(*)的变量名会存放所以未命名的变量参数。    
"""
print("不定长参数")


def printinfoTuple(arg=10, *vartuple):
    print("arg:", arg)
    for var in vartuple:
        print(var)
    return


printinfoTuple(10, 20, 30)

# lambda
print("lambda表达式")
sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为：", sum(10, 20))

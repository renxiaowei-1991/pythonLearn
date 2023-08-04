#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

"""
lambda表达式
    匿名函数
    python使用lambda来创建匿名函数
        lambda只是一个表达式，函数体比def简单很多
        lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
        lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
        虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
语法：
    lambda [arg1 [,arg2,...argn]]:expression


"""


def lambdaFun():
    """
    解释：
        lambda 表达式，以x作为参数，进行计算。
        计算公式 (x**2 + x*5 - x)
            x的2次方 + x乘以5 - x
        -4作为参数传给x
    """
    y = (lambda x: x ** 2 + x * 5 - x)(-4)
    print(y)

    triple = lambda x: x * 3
    add = lambda x, y: x + y
    z = add(triple(3), 4)
    print(z)
    print(triple(3))


if __name__ == "__main__":
    lambdaFun()
    
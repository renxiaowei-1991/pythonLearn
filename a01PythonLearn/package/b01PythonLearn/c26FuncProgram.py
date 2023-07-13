#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time

"""
函数式编程
    基于函数的一种编程风格。
    函数式编程的关键部分是高阶函数。可以将函数当成对象看待。
    高阶函数将其他函数作为参数，或者将其作为结果返回

    纯函数：函数内部操作不影响函数外部变量
    非纯函数：函数内部操作影响到了函数外部的变量

    map
        内置函数map是在列表(迭代对象)上运行的非常有用的高阶函数。
        函数map接受一个函数和一个迭代器作为参数，并返回一个新的迭代器。该函数应用于每个参数
        语法：
            map(function, iterable)
            function:函数名
            iterable:迭代对象(列表,元组...)

    filter
        内置函数filter通过删除与谓词(一个返回布尔值的函数)不匹配的项来过滤一个迭代。
        获取迭代对象(列表)中所有满足filter_test判断的数据，结果是filter对象，需要转换为list对象
        语法：
            filter(function, iterable)
            function:函数名
            iterable:迭代对象(列表,元组...)

lambda表达式
    匿名函数
    python使用lambda来创建匿名函数
        lambda只是一个表达式，函数体比def简单很多
        lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
        lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
        虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
    语法：
        lambda [arg1 [,arg2,...argn]]:expression


生成器：
    生成器允许声明一个像迭代器一样的函数，可以在for循环中使用
    生成器是一种可迭代的类型，如列表或元组。
    与列表不同的是，生成器不允许使用任意索引，但是仍然可以通过for循环迭代
    可以使用函数+yield语句创建生成器
    yield：
        yield语句用于定义一个生成器，替换函数的返回值，以向调用者提供结果而不破坏局部变量。

    生成器一次产生一个项目，所以生成器不具有列表的内存限制。
    生成器是一种创建迭代对象的简单方法。不使用生成器也可以创建迭代对象。
    next()
        可以使用next对生成器进行迭代

    注意：
        生成器可以提高性能，降低内存使用率，在开始使用之前，不需要等到所以的元素都被生成(生成器函数在运行的时候，时刻在返回值，生成一个就可以使用一个)。
        通过控制生成器生成元素的时间，可以看出生成器在使用的时候是生成一个，使用一个。也可以通过生成器控制程序执行
            time.sleep(3) #休眠3秒


装饰器
    用于修改其它函数的功能，对原函数进行功能扩展。
    一个函数可以被多个装饰器函数装饰。
    @symble 用@的方式对函数添加装饰器
    
    常见装饰器
        @classmethod: 声明一个类方法，可以通过类名直接调用。
        @staticmethod: 声明一个静态方法，可以通过类名直接调用。
        @property: 将一个方法转换为只读属性。
        @abstractmethod: 声明一个抽象方法，子类必须实现它。
        @wraps: 用于保留原始函数的元数据（如函数名、注释等）。
        @retry: 在发生错误时自动重试代码块一定次数。
        @login_required: 用于限制需要用户登录才能访问的视图函数。
        @cache: 缓存函数的结果，避免重复计算。


递归
    递归的基本部分是自引用-调用自己的函数(函数可以调用自己)。
    递归被用来解决可以被分解成相同类型的更容易的子问题的问题。
    一个递归实现的函数的典型例子是阶乘函数，N的阶乘写作N!，表示小于等于N的所有正整数的乘积
    样例：
        5! = 5 * 4 * 3 * 2 * 1
        5! = 5 * 4!
        4! = 4 * 3!
        3! = 3 * 2!
        2! = 2 * 1!
        1! = 1(基准情形)
    基准情形：当做退出条件。要不会一直循环

"""

"""
函数式编程
"""
def apply_twice(func, args):
    return func(func(args))

def add_five(x):
    return x + 5


# 纯函数
def pure_func(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)


# 非纯函数:修改了函数外部的some_list
def impure(arg):
    some_list.append(arg)


"""
lambda练习
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


"""
内置高阶函数
    map
    filter
"""
def map_test(x):
    return x + 5

def filter_test(x):
    return x % 2 == 0


"""
生成器：
    通过函数和yield语句，人为创建一个可迭代对象，作为一个函数返回值
"""
# 生成器构建
def countdown():
    """
    返回的结果是一个使用i构建的生成器。内容是(5, 4, 3, 2, 1)
    """
    i = 5
    while i > 0:
        yield i
        i -= 1

def countdown1():
    """
    返回的结果是一个使用i构建的生成器。内容是(5, 4, 3, 2, 1)
    """
    for i in range(1, 100000):
        yield i
        # 休眠3秒
        time.sleep(3)


"""
装饰器：
	用于修改其它函数的功能，对原函数进行功能扩展。
	一个函数可以被多个装饰器函数装饰
"""
def docer1(func):
    """
    装饰器1
    :param func:
    :return:
    """
    def warp():
        print("装饰器测试1")
        func()
        return
    return warp

def docer2(func):
    """
    装饰器2
    :param func:
    :return:
    """
    def warp():
        print("装饰器测试2")
        func()
        return
    return warp


# 1、装饰器方式调用
#   这种装饰器调用方式是从下往上嵌套，也就是从内往外嵌套。
#   就是先用docer2装饰，再用docer1装饰
@docer1
@docer2
def test_func1():
    print("Hello World")


# 2、普通方式调用(和上面装饰器的方式等价，但是写法上比较麻烦)
def test_func2():
    print("Hello World")


"""
递归
"""
def factorial(x):
    """
    计算x的阶乘
    :param x:
    :return:
    """
    if x == 1:
        # 退出条件
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == "__main__":
    # 函数式编程
    print(apply_twice(add_five, 20))

    some_list = []

    # lambda练习
    lambdaFun()

    # 内置高阶函数
    # map
    lista = [11, 22, 33, 44, 55]
    print(list(map(map_test, lista)))
    #使用lambda作为参数，使用map加工列表数据
    print(list(map((lambda x: x + 5), lista)))

    # filter
    # 获取lista中所有满足filter_test判断的数据，结果是filter对象，需要转换为list对象
    print(list(filter(filter_test, lista)))
    # 使用lambda作为参数，使用filter加工列表数据
    print(list(filter((lambda x: x % 2 == 0), lista)))

    # 对生成器进行迭代
    print("生成器测试")
    print(next(countdown()))
    print(next(countdown()))
    for i in countdown():
        print(i, end=" ")
    print(list(countdown()))
    # print(list(countdown1()))
    # 通过控制生成器生成元素的时间，可以看出生成器在使用的时候是生成一个，使用一个。也可以通过生成器控制程序执行
    # for i in countdown1():
    #     print(i)
    print("使用高阶函数map，对使用函数+yield语句构建的生成器(迭代对象)中的所有元素，做lambda匿名函数的操作。将返回的结果map对象，通过list转换成列表")
    print(list(map((lambda x: x * 3), countdown())))
    print("使用高阶函数filter，对使用函数+yield语句构建的生成器(迭代对象)中的所有元素，做lambda匿名函数的判断。将返回的结果filter对象，通过list转换成列表")
    print(list(filter((lambda x: x % 2 == 0), countdown())))

    # 1、装饰器方式调用
    #   这种装饰器调用方式是从下往上嵌套，也就是从内往外嵌套。
    #   就是先用docer2装饰，再用docer1装饰
    print("测试方法1")
    test_func1()

    # 2、普通方式调用(和上面装饰器的方式等价，但是写法上比较麻烦)
    print("测试方法2")
    test_func2 = docer2(test_func2)
    test_func2()
    test_func2 = docer1(test_func2)
    test_func2()

    # 递归
    print("5的阶乘 =", factorial(5))

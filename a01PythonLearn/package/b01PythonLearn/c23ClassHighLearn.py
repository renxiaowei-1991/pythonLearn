# /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import math
from functools import reduce
from functools import wraps

"""
迭代器
    迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退

    迭代器有两个基本的方法：
        iter()  创建迭代器
        next()  获取迭代器的下一个元素

    字符串、列表、元组对象 都可用于创建迭代器

    迭代器结束的异常
        StopIteration

创建迭代器
    把一个类作为一个迭代器使用需要在类中实现两个方法__iter__() 与 __nexe__()
    __iter__()方法返回一个特殊的迭代器对象，这个迭代器对象实现了__next__()方法并通过StopIteration异常标识迭代的完成。
    __next__()方法会返回下一个迭代器对象

    只有实现了__iter__()，才能在使用iter()的时候创建一个迭代器
    只有实现了__next__()，才能在使用next()的时候通过__next__()按照规则获取下一个值
"""

"""
实现了迭代器函数的类
"""


class iterationNum:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        # 需要先把self.a保存返回，再加1
        x = self.a
        self.a += 1
        return x


"""
迭代器的多种使用方式
"""


def mapLearn():
    list = [1, 2, 3, 4]  # 列表
    print("迭代器使用方式01")
    mapL01 = iter(list)  # 使用列表创建迭代器
    for mapl in mapL01:
        # print(mapl)
        # 使用end修改输出的最后字符，这里将换行替换为空格
        print(mapl, end=" ")

    print("迭代器使用方式02")
    # 迭代器输出完后，不能在用next，否则会报错StopIteration
    mapL02 = iter(list)  # 使用列表创建迭代器
    print(next(mapL02))
    print(next(mapL02))
    print(next(mapL02))
    print(next(mapL02))
    # print(next(mapL02))

    print("迭代器使用方式03")
    mapL03 = iter(list)  # 使用列表创建迭代器
    # i = True
    # while i:
    #     try:
    #         mapl03 = next(mapL03)
    #         print(mapl03)
    #     except StopIteration:
    #         i = False
    #         print("迭代器03已遍历结束")

    while True:
        try:
            print(next(mapL03))
        except StopIteration:
            break
            print("迭代器03已遍历结束")

    print("迭代器对象创建及使用")
    itClass = iterationNum()
    itN = iter(itClass)
    # while True:
    #     try:
    #         b = next(itN)
    #         if b == 10:
    #             break;
    #         else:
    #             print(b)
    #     except StopIteration:
    #         break

    while True:
        try:
            print(next(itN))
        except StopIteration:
            break


"""
生成器
    用于生成迭代器
    在Python中，使用yield的函数被称为生成器(generator)
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作。
    简单理解：生成器就是一个迭代器
    调用一个生成器函数，返回的是一个迭代器对象

    在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行。
    使用yield生成迭代器需要配合循环使用

    所谓生成器就是利用循环将某个变量或某个值整合到一起，作为一个迭代器返回
    也可以理解为将想要的数整合到一起，作为一个迭代器返回

"""
"""
生成器函数
    斐波那契数列
"""


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


"""
生成器函数练习
    使用yield生成迭代器，需要配合循环使用
"""


def yieldTest(n):
    i = 0
    while True:
        yield i
        if i <= n:
            i += 1
        else:
            return


"""
生成器的使用练习
"""


def yieldLearn():
    print("通过生成器实现:斐波那契数列")
    fi = fibonacci(10)
    while True:
        try:
            print(next(fi))
        except StopIteration:
            break

    print("自定义生成器实现")
    yt = yieldTest(10)
    while True:
        try:
            print(next(yt))
        except StopIteration:
            break


"""
map&filter&reduce
    函数式编程的代表

    内置函数map和filter是在列表(或类似的称为迭代的对象)上运行的非常有用的高阶函数
    函数map接受一个函数和一个迭代器作为参数，并返回一个新的迭代器，该函数应用于每个参数

map()
    使用迭代器按指定规则生成迭代器
    根据提供的函数对指定序列做映射

    语法:
        map(function, iterable, ...)
        参数:
            function  函数
            iterable  一个或多个序列
        返回值:
            Python2.x 返回列表
            Python3.x 返回迭代器
        解释：
            第一个参数function以参数序列iterable中的每一个元素调用function函数
            返回包含每次function函数返回值的新列表

"""
"""
函数式编程map()高阶函数的练习
"""
"""
定义一个函数用于测试map
    计算平方数
"""


def square(x):
    return x ** 2


"""
map()使用练习
"""


def mapLearn():
    list = [1, 2, 3, 4, 5]
    # 对list中的每一个元素按照square进行处理，并返回结果集，作为迭代器返回
    print("使用函数实现map()")
    mL01 = map(square, list)
    for ml in mL01:
        print(ml)

    # 使用lambda实现
    print("使用lambda表达式实现map()")
    mL02 = map(lambda x: x ** 2, list)
    while True:
        try:
            print(next(mL02))
        except StopIteration:
            break

    """
    使用两个列表作为两个参数
    使用lambda接受两个参数进行map()计算
    """
    print("使用lambda计算两个迭代器实现map()")
    listX = [1, 2, 3, 4, 5]
    listY = [-1, -2, -3, -4, -5]
    mL03 = map(lambda x, y: x + y, listX, listY)
    for ml03 in mL03:
        print(ml03)


"""


filter()
    filter()函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表

    语法：
        filter(function, iterable)
        参数：
            function  判断函数
            iterable  可迭代对象
        返回值：
            Python2.x 返回列表
            Python3.x 返回可迭代对象
        解释：
            接收两个参数，第一个是函数，第二个是序列，序列的每个元素作为参数传递给函数进行判断。
            然后返回True或False，最后将返回True的元素放到新列表中


"""
"""
函数式编程filter()高阶函数的练习
"""
"""
定义一个函数用于测试filter
    判断是否单数
"""


def isOdd(n):
    return n % 2 == 1


"""
filter使用练习
"""


def filterLearn():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("使用函数实现filter")
    fL01 = filter(isOdd, list)
    for fl in fL01:
        print(fl)

    print("使用lambda实现filter")
    fL02 = filter(lambda x: x % 2 == 1, list)
    while True:
        try:
            print(next(fL02))
        except StopIteration:
            break

    print("使用filter过滤除1~100中平方根是整数的数")
    fL03 = filter(lambda x: math.sqrt(x) % 1 == 0, range(1, 101, 1))
    for fl03 in fL03:
        print(fl03)


"""
reduce()
    reduce()函数会对参数序列中元素进行累积

    语法：
        reduce(function, iterable[, initializer])
        参数：
            function     函数，有两个参数
            iterable     可迭代对象
            initializer  可选，初始参数
        返回值：
            函数计算结果
        解释：
            函数将一个数据集合(链表，元组等)中的所有数据进行下列操作：
                用传给reduce中的函数function(有两个参数)先对集合中的第1、2个元素进行操作
                得到的结果再与第三个数据用function函数运算，最后得到一个结果
            也就是说把iterable中的所有值进行function计算，得到一个计算结果
        注意：
            Python3.x reduce()已经被移动到functools模块里，如果要使用，需要引入functools模块来调用reduce()函数
            from functools import reduce

"""
"""
函数式编程reduce()高阶函数的练习
"""
"""
定义一个函数用于测试reduce
    加法
"""


def addRed(x, y):
    return x + y


"""
reduce使用练习
"""


def reduceLearn():
    list = [1, 2, 3, 4, 5]
    rL01 = reduce(addRed, list)
    print("使用函数实现reduce")
    print(rL01)

    print("使用lambda实现reduce")
    rL02 = reduce(lambda x, y: x + y, list)
    print(rL02)

    print("使用reduce计算1-100的和")
    rL03 = reduce(lambda x, y: x + y, range(1, 101, 1))
    print(rL03)

    print("使用reduce计算1-100的积")
    rL04 = reduce(lambda x, y: x * y, range(1, 101, 1))
    print(rL04)


"""
装饰器
    装饰器(Decorators)是Python的一个重要部分。
    简单的说：他们是修改其他函数的功能的函数。
    有助于让代码更简单，更Pythonic(Python范儿)。
    需要知道在哪里使用装饰器，已经如何开发装饰器。

    装饰器是得在一个函数的前后执行代码
    工厂模式？

    装饰器就是定义一个嵌套函数，已一个函数作为参数，在嵌套函数中把参数函数前后加一下语句，然后把嵌套函数作为返回值。这样就相当于修改了参数函数的功能

装饰器包装
    functools.wraps 装饰器修饰函数 
    @wraps
        接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等功能。
        这可以让我们在装饰器里面访问在装饰之前的函数的属性

    @装饰器名称
        在函数前面加@+装饰器名称，表示使用指定的装饰器对该函数进行装饰。
        在后面使用该函数的是，就是已经经过装饰的功能了

装饰器常用实现
    授权检查
    日志实现
    装饰器类
    发送邮件
    ...

装饰器定义及使用标准语句
    from functools import wraps
    def decorator_name(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not can_run:
                return "Function will not run"
            return f(*args, **kwargs)
        return decorated

    @decorator_name
    def func():
        return("Function is running")

    can_run = True
    print(func())
    # Output: Function is running

    can_run = False
    print(func())
    # Output: Function will not run

函数
    函数可以赋值
    函数中可以定义函数(函数中定义的函数，在函数外无法访问)
    函数可以返回函数

    funcName()  执行函数
        funcName()
    funcName    把函数整体赋值给另外一个变量
        a1 = funcName
        a1()

"""

"""
一切皆对象
"""
"""
函数赋值使用实例
"""


def hi(name="renxw"):
    return "hi " + name


"""
函数中定义函数
    函数中定义的函数，在函数外不能被访问
"""


def hiFun01(name="renxw"):
    print("now you are inside the hiFun01() function")

    def hiFun02():
        return "now you are in the hiFun02() function"

    def hiFun03():
        return "now you are in the hiFun03() function"

    print(hiFun02())
    print(hiFun03())
    print("now you are back in the hiFun01() function")


"""
从函数中返回函数
"""


def hiFun04(name="renxw"):
    print("now you are inside the hiFun04() function")

    def hiFun02():
        return "now you are in the hiFun02() function"

    def hiFun03():
        return "now you are in the hiFun03() function"

    if name == "renxw":
        return hiFun02
    else:
        return hiFun03


"""
函数练习
"""


def hiFunTest():
    print("函数赋值")
    print(hi())
    hi01 = hi
    print(hi01())
    # 可以删除hi01，删除hi报错
    # del hi01
    # del hi
    # print(hi())
    # print(hi01())

    print("在函数中定义函数")
    hiFun01()

    print("从函数中返回函数")
    hiFun05 = hiFun04()
    print(hiFun05())


"""
装饰器练习
"""
"""
装饰器函数定义
    functools.wraps 指明装饰的函数
@wraps(a01Fun)
    接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等功能。
        这可以让我们在装饰器里面访问在装饰之前的函数的属性
"""


def a01Decorator(a01Fun):
    @wraps(a01Fun)
    def wrapTheFunction():
        print("I am doing some boring work before executing a01Fun()")
        a01Fun()
        print("I am doing some boring work after executing a01Fun()")

    return wrapTheFunction


"""
@指明装饰器
在指明装饰器后，在使用函数的时候就可以直接使用装饰后的功能，不需要再使用装饰器进行包装赋值了
"""


@a01Decorator
def a02Fun():
    print("I am the function which needs some decoration to remove my foul smell")


"""
装饰器练习
"""


def decoratorLearn():
    a02Fun()
    print(a02Fun.__name__)
    # a03Fun = a01Decorator(a02Fun)
    # a03Fun()
    # print(a03Fun.__name__)


"""
递归练习
    x!  x的阶乘的实现
"""


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


"""
递归练习
"""


def recursionLearn():
    print(factorial(10))


if __name__ == "__main__":
    # print("迭代器练习")
    # mapLearn()
    # print("生成器练习")
    # yieldLearn()
    # print("函数式编程高阶函数-map练习")
    # mapLearn()
    # print("函数式编程高阶函数-filter练习")
    # filterLearn()
    # print("函数式编程高阶函数-reduce练习")
    # reduceLearn()
    # print("函数练习")
    # hiFunTest()
    # print("装饰器练习")
    # decoratorLearn()
    print("递归练习")
    recursionLearn()
    
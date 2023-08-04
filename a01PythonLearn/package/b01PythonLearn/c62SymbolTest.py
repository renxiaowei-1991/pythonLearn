#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from functools import wraps
from functools import reduce
import itertools


"""
迭代器
迭代器类
生成器
装饰器

"""


class NumIter:
    """迭代类"""
    def __init__(self):
        pass

    def __iter__(self):
        self.num = 1
        # 迭代器迭代的是对象。所以这里需要返回self。self表示对象
        return self

    def __next__(self):
        # 需要先把self.num保存，用于后序返回，然后再+1。否则开始的地方就不是1了。就是2了
        x = self.num
        self.num += 1
        return x


def iter_func():
    """
    迭代器测试
    :return:
    """
    """迭代器测试-类1"""
    iter_1 = iter(NumIter())
    print(next(iter_1))
    print(next(iter_1))
    print(next(iter_1))
    print(next(iter_1))

    """迭代器测试-类2"""
    iter_2 = iter(NumIter())
    for i in iter_2:
        if i <= 10:
            print(i)
        else:
            # 需要break结束，否则会一直执行。需要手动控制结束
            break

    """迭代器测试-列表1"""
    lista = [1, 2, 3, 4, 5]
    for i in lista:
        print(i)

    """迭代器测试-列表2"""
    for i in iter(lista):
        print(i)

    """迭代器测试-列表3"""
    iter_lista = iter(lista)
    while True:
        try:
            print(next(iter_lista))
        except StopIteration:
            print("迭代越界")
            # 迭代越界后需要手动跳出循环
            break

    """迭代器测试-元组1"""
    tuplea = (1, 2, 3, 4, 5)
    for i in tuplea:
        print(i)

    """迭代器测试-元组2"""
    iter_tuplea = iter(tuplea)
    for i in iter_tuplea:
        print(i)

    """迭代器测试-字典1"""
    dicta = {"name": "rxw", "age": 31, "sex": "男"}
    for i in dicta.values():
        print(i)

    iter_dicta = iter(dicta.values())
    for i in iter_dicta:
        print(i)


def yield_func():
    """
    迭代器测试1
    :return:
    """
    num_iter = iter(NumIter())
    for num in num_iter:
        if num <= 100:
            # yield替换return，作为返回值
            yield num
        else:
            break


def yield_num():
    # 生成器，没3秒生成一个值。用于测试是否是生成一个就可以使用一个
    for i in range(0, 10000):
        time.sleep(1)
        yield i


def wraps_func(fun):
    """用于标志装饰器，并且应用fun函数"""
    @wraps(fun)
    def print_func_wraps(*args, **kwargs):
        print("func is print_func_wraps")
        def fun(*args, **kwargs):
            for i in args:
                print(i)
            for i in kwargs:
                print(i)
            return
        fun(*args, **kwargs)
    return print_func_wraps


@wraps_func
def print_func():
    print("func is print_func")


def wraps_func1(max_retries=3, timeout=1):
    """
    定义装饰
    用于标志装饰器，并且应用fun函数
    返回函数名的方式是函数式编程的功能
    max_retries: 传给装饰器本身的参数
    timeout: 传给装饰器本身的参数
    """
    def decorator(fun):
        """
        定义真正的装饰器
        fun 用于接收被装饰函数
        """
        def wrapper(*args, **kwargs):
            """
            用于实现被装饰函数功能
            :param args: 用于接收被装饰函数的所有非关键字参数
            :param kwargs: 用于接收被装饰函数的所有关键字参数
            :return:
            """
            print("func is print_func_wraps")
            print("args:")
            for i in args:
                print(i)
            print("kwargs:")
            for key, value in kwargs.items():
                print(key, value)
            """
            将通过wrapper接收到的被装饰函数本身的参数，再次传递给被装饰函数
            执行被装饰函数
            并且返回被装饰函数的返回值
            """
            return fun(*args, **kwargs)
        """返回被装饰之后的函数名"""
        return wrapper
    """返回装饰器函数名"""
    return decorator


@wraps_func1(max_retries=3, timeout=1)
def wraps_func1(name, age):
    print("func is print_func")
    # 装饰器无法处理被装饰函数的返回值
    return "name=", name, ",age=", age


def retry(max_retries=3, timeout=1):
    """
    定义装饰：用于函数重试，和等待重试时长。
    这里面的参数时装饰器函数本身的参数
    :param max_retries: 最大重试次数
    :param timeout: 设置超时重试时长
    :return:
    """
    def decorator(func):
        """
        定义装饰器和将装饰器返回
        :param func: 以函数式编程的方式，使用参数接收被装饰函数的函数名，在装饰器中使用 func() 进行执行函数
        :return: wrapper(被装饰之后的函数名，在函数被装饰之后，调用别装饰函数的时候，实际上调用的就是wrapper函数)
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            定义被装饰函数，被装饰之后的函数功能
            这里的参数时被装饰函数的参数
            @wraps(func): 这里可以使用wraps用来标识装饰器，并且接收func函数名。不写也可以
            @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
            :param args: (形参)(元组)用于接收被装饰函数的所有非关键字参数
            :param kwargs: (形参)(字典)用于接收被装饰函数的所有关键字参数
            :return:
            """
            """使用循环的方式对被装饰函数进行重试"""
            retries = 0
            exce_type = 0
            while retries < max_retries:
                try:
                    """
                    args: (实参)将通过wrapper函数接收到的被装饰函数的非关键字参数的参数集合(元组)，使用*进行展开，将其中所有元素单独传递给被装饰函数
                    kwargs: (实参)将通过wrapper函数接收到的被装饰函数的关键字参数的参数集合(字典)，使用**进行展开，将其中所有元素(键:值对)单独传递给被装饰函数
                    1、将被装饰函数所有参数传递给被装饰函数
                    2、执行被装饰函数
                    3、返回被装饰函数的return值(被装饰函数的返回值需要单独返回，要不然无法被引用)
                    注意点：
                        如果func执行没有异常，就会直接执行return语句将func结果返回，那就不会再进行循环了。而不会在func正常的情况下还将func循环执行三次
                    """
                    return func(*args, **kwargs)
                except BaseException as e:
                    """重试次数+1"""
                    retries += 1
                    """最后失败时，将失败原因进行保存，进行输出！"""
                    exce_type = e if retries == max_retries else None
                    """输出失败日志"""
                    print(f"执行 {func.__name__} 失败，正在进行第 {retries} 次重试！")
                    """失败重试，等待时间"""
                    time.sleep(timeout)
            """
            最终失败后将异常抛出，并且将失败信息进行提示！
            异常抛出的时候使用之前存储好的异常遍历，获取异常类型，准确的进行异常信息输出
            """
            raise exce_type.__class__(f"执行 {func.__name__} 失败，已达到最大重试次数，最终的失败原因是 {exce_type}！")
        """函数式编程:将被装饰器装饰后的的函数名返回"""
        return wrapper
    """函数式编程:将装饰器函数的函数名返回"""
    return decorator


@retry(max_retries=3, timeout=1)
def retry_test():
    """
    @retry: 使用装饰器retry对函数进行装饰
    max_retries: 传递给装饰器的参数
    timeout: 传递给装饰器的参数
    :return:
    """
    print("retry测试")
    raise(IOError, "主动抛出异常，用于装饰器测试！")
    return 1


@retry(max_retries=10, timeout=3)
def sum_num(x, y):
    a = x + y
    # raise (IOError, "主动抛出异常，用于装饰器测试！")
    return a


if __name__ == "__main__":
    iter_func()
    """生成器测试-1"""
    print(list(yield_func()))
    """生成器测试-2"""
    for i in yield_num():
        if i <= 1:
            print(i)
        else:
            break

    """装饰器测试-1"""
    print_func("rxw", 123)
    """装饰器测试-2"""
    print(wraps_func1(name="rxw", age=31))
    """装饰器测试-3"""
    print(retry_test())
    """装饰器测试-4"""
    print(sum_num(3, 4))

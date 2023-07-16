#!/usr/bin/env python
# -*- coding:utf-8 -*-

import functools
import itertools
import os
import sys
import time


"""
用于组织自定义装饰器
"""


def retry(max_retries=3, timeout=1):
    """
    功能：重试功能装饰器
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
        @functools.wraps(func)
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
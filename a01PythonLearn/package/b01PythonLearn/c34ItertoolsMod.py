#!/usr/bin/env python
# coding:utf-8

import itertools

"""
内建模块: itertools
    itertools模块是一个标准库，包含了几个在函数编程中很有用的函数。
    
    无限迭代器：itertools其中一种函数类型
        count(num, step) : count函数从一个值开始无限增加(如果不指定num和step(步长)，默认从0开始，步长1)
        cycle() : cycle函数无限次迭代(例如：列表或字符串)(对列表或字符串等无限次循环，每次处理的数据就是列表或者字符串本身)
        repeat() : repeat函数重复一个对象，无论是无限还是特定的次数
        
    itertools中有许多功能可以在迭代器上运行，类似于映射和过滤
        takewhile() : 当判定函数(返回值为True或False)保持为True时，从迭代中取得项目
            使用函数编程的高阶函数 filter 效果一样
        chain() : 将几个迭代结合成一个长整数
            可以将不同类型的迭代进行整合。整合后是object，可以使用list转换成列表
            例如：可以将 列表+元组+字典+集合 整合在一起
        accumulate() : 以可迭代的方式返回一个正在运行的值
            可以使用函数式编程的高阶函数map+递归函数定义实现accumulate的功能
            
    itertools还有几个组合函数，可以完成项目的所有可能的组合。
        product() : 
            多个对象中所有元素的组合。第一个对象元素放前面，第二个对象的元素放后面
            样例：
                aa = ("a", "b")
                bb = range(5)
                list(itertools.product(("a", "b"), range(5)))
                结果：[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('b', 4)]
    
        permutation() : 
            对象中元素的所有组合。没有前后顺序。
            例如：
                aa = ("a", "b")
                list(itertools.permutations(aa))
                结果：[('a', 'b'), ('b', 'a')]
            注意：
                itertools.permutations() 只能有一个参数

"""


def itertools_count():
    """
    itertools.count() 练习
    :return:
    """
    print(type(itertools.count()))
    for i in itertools.count(3, 3):
        print(i)
        if i >= 100:
            break
    return


def itertools_cycle():
    """
    itertools.cycle() 练习
    :return:
    """
    count = 0
    cycle_list = ""
    for i in itertools.cycle("abc"):
        cycle_list += i
        if count >= 100:
            break
        else:
            count += 1
    print(cycle_list)

    count = 0
    cycle_list = []
    for i in itertools.cycle([1, 2]):
        cycle_list.append(i)
        if count >= 100:
            break
        else:
            count += 1
    print(cycle_list)
    return


def itertools_repeat():
    """
    itertools.repeat() 练习
    :return:
    """
    print(itertools.repeat("abc", 3))
    print([i for i in itertools.repeat("abc", 3)])
    for i in itertools.repeat("abc", 3):
        print(i)
    for i in itertools.repeat([1, 3, 4], 3):
        print(i)
    print([i for i in itertools.repeat([1, 3, 4], 3)])


"""
a(0) : 0
a(1) : a(0) + 1
a(2) : a(1) + 2
a(3) : a(2) + 3
a(4) : a(3) + 4
a(5) : a(4) + 5
a(6) : a(5) + 6
a(7) : a(6) + 7
"""
def itertools_accumulate():
    """
    itertools.accumulate() 练习
        相同的功能可以使用函数式编程的高阶函数map+递归函数定义实现
    :return:
    """
    print("可以使用函数式编程的高阶函数map+递归函数定义实现accumulate的功能")
    def add_01(x):
        if x == 0:
            return 0
        else:
            return add_01(x - 1) + x
    nums1 = list(map(lambda x: add_01(x), range(8)))
    print("nums1:", nums1)
    nums = list(itertools.accumulate(range(8)))
    print("nums:", nums) # [0, 1, 3, 6, 10, 15, 21, 28]
    return


def itertools_takewhile():
    """
    itertools.takewhile()
        功能类似高阶函数filter
    :return:
    """
    def add_01(x):
        if x == 0:
            return 0
        else:
            return add_01(x - 1) + x
    nums1 = list(map(lambda x: add_01(x), range(8)))
    print("nums1:", nums1)
    nums = list(itertools.accumulate(range(8)))
    print("nums:", nums)  # [0, 1, 3, 6, 10, 15, 21, 28]
    # 使用函数编程的高阶函数 filter 效果一样
    print(list(itertools.takewhile(lambda x: x <= 6, nums)))
    print(list(filter(lambda x: x <= 6, nums)))


def itertools_chain():
    """
    itertools.chain(var1, var2, ...)
        可以将不同类型的迭代进行整合。整合后是object，可以使用list转换成列表
        例如：可以将 列表+元组+字典+集合 整合在一起
    :return:
    """
    lista = [1, 2, 'a']
    tuplea = (2, 4, 'b')
    dicta = {"name": "rxw", "age": 31}
    seta = {"rxw", 31, 18}
    print(list(itertools.chain(lista, tuplea, dicta, seta)))


def itertools_product():
    """
    多个对象中所有元素的组合。第一个对象元素放前面，第二个对象的元素放后面
    aa = ("a", "b")
    bb = range(5)
    list(itertools.product(("a", "b"), range(5))) # [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('b', 4)]
    :return:
    """
    print("product:", list(itertools.product(("a", "b"), range(5))))
    return


def itertools_permutation():
    """
    对象中元素的所有组合
    例如：
        aa = ("a", "b")
        list(itertools.permutations(aa)) # [('a', 'b'), ('b', 'a')]
    注意：
        itertools.permutations() 只能有一个参数
    :return:
    """
    aa = ("a", "b")
    bb = ("1", "2")
    print("permutation:", list(itertools.permutations(aa)))
    # 只能有一个参数
    # print("permutation:", list(itertools.permutations(aa, bb)))
    return

if __name__ == "__main__":
    itertools_count()
    itertools_cycle()
    itertools_repeat()
    itertools_accumulate()
    itertools_takewhile()
    itertools_chain()
    itertools_product()
    itertools_permutation()

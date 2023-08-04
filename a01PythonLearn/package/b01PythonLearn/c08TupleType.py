#!/use/bin/env python
# -*- coding:utf-8 -*-

import math

"""
    元组
        与列表类似，使用()
        元组中只包含一个元素时，需要在元素后面添加逗号
        元组中的元素值不允许修改，但是可以对元组进行连接组合
        元组计算和列表类似

    删除元组
        del tup

    任何无符号的对象，以逗号隔开，默认为元组

    函数&方法
        tuple(seq)  将列表转换为元组


"""
print("创建元组")
tup1 = ()
tup2 = (50,)
tup3 = tup1 + tup2
print(tup1, tup2, tup3)
del tup1
# print(tup1,tup2,tup3)
tup4 = '123', 'abc', 234, 45.6
print(tup4)
tup5 = ['123', 'abc', 234, 45.6]
print(tuple(tup5))

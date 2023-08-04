#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

"""
math.pi
    Π:3.14159265...

r ** 3
    r的三次方(r * r * r)

r ** 2
    r的二次方(r * r)

r ** n
    r的n次方

"""


def math_test():
    r = 2
    print("r ** 3 =", r ** 3)
    print("r ** 2 =", r ** 2)
    print("球的体积：", 4/3 * math.pi * r ** 3)
    print("球的面积：", 4 * math.pi * r ** 2)


if __name__ == "__main__":
    math_test()
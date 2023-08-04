#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
from package.b02BaseModule import c01SQLFunc


if __name__ == "__main__":
    # project_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\"
    # 将工程所在根目录添加到path环境变量中，已防止在绝对应用中出现找不到package的情况(doc环境执行的时候，如果没有修改环境变量，会出这种情况)
    # sys.path.append(project_path)
    # 设置PYTHONPATH变量，把当前工程根目录加到PYTHONPATH中，就可以避免绝对应用在doc环境下找不到路径的问题了。设置完成后重新打开doc环境，重新执行py脚本即可
    print(sys.path)
    # from package.a02PkgImpTest import c01SQLFunc
    # from package.a02PkgImpTest.c02PkgImpTest import d01PkgImpTest
    # print(sys.__dir__())
    # print(os.__dir__())
    # print(sys.__name__)
    # print(os.__name__)
    # print(__name__)
    # print(__file__)
    # print(os.getcwd())
    # print(os.path.dirname(__file__))
    # print(sys.path)
    # 在pycharm中执行的时候，不需要使用下面的语句修改path环境变量，pycharm会自动处理
    # 如果在doc执行程序，需要使用下面的语句拿到工程所在根目录，将路径加入到path环境变量中，否则会导致package包在环境变量找不到，从而无法进行导入，导致报错
    # print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    # sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    print(c01SQLFunc.date_add("2023-06-21", 10))
    print(c01SQLFunc.date_sub("2023-06-21", 10))
    print(c01SQLFunc.add_months("2023-06-30", -4))
    print(c01SQLFunc.get_month_start("2023-06-21"))

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

"""
主要的第三方库
    Python 标准库本身包含广泛的功能。
    但是，有些任务需要使用第三方库。一些主要的第三方库：
    Django：用 Python 编写的最常用的 Web 框架，Django 支持包含 Instagram 和 Disqus 的网站。它有很多有用的功能，它所缺少的功能都被扩展包所覆盖。
    CherryPy 和 Flask 也是流行的 Web 框架。
    为了从网站上抓取数据，BeautifulSoup 库非常有用，并且比使用正则表达式构建自己的过滤机制效果更好。

    虽然 Python 确实提供了以编程方式访问网站的模块，比如 urllib，但它们使用起来相当麻烦。第三方库请求使得 HTTP 请求更容易使用

    Python 可以使用许多第三方模块使科学计算和数学计算变得更容易。
    matplotlib 模块允许你在Python中创建基于数据的图形。
    NumPy 模块允许使用比嵌套列表的本地 Python 解决方案快得多的多维数组。它还包含执行数学运算的功能，如阵列上的矩阵变换。
    SciPy 库包含许多对 NumPy 的扩展。

    Python 也可以用于游戏开发。
    通常，它被用作用其他语言编写的游戏的脚本语言，但它可以用来自己制作游戏。
    3D 游戏，可以使用 Panda3D 库。2D 游戏，你可以使用 pygame。
"""

"""
打包
    在 Python 中，术语打包指的是将模块写成标准格式，以便其他程序员可以轻松安装和使用它们。
    这包括使用模块 setuptools 和 distutils。
    打包第一步是正确组织现有文件。将所有要放入库的文件放在同一个父目录中。
    该目录还应该包含一个名为 __init__.py 的文件，该文件可以是空白的，但必须存在于目录中。
    示例目录结构：    
        W3Cschool/
            LICENSE.txt
            README.txt
            setup.py
            w3c/
                __init__.py
                w3cschool.py
                w3cschool2.py

    __init__.py 文件的作用是什么呢？
        __init__.py 最明显的作用就是使包和普通目录区分；其次可以在该文件中申明模块级别的import语句从而使其变成包级别可见。

    打包的下一步是编写 setup.py 文件。
    这包含组装软件包所需的信息，以便将其上传到 PyPI 并使用 pip （名称，版本等）进行安装。
    setup.py 文件的示例：
        from distutils.core import setup

        setup(
           name='W3Cschool', 
           version='0.1dev',
           packages=['w3cschool',],
           license='MIT', 
           long_description=open('README.txt').read(),
        )
    创建 setup.py 文件后，将其上传到 PyPI，或使用命令行创建二进制分发（可执行安装程序）。
    要构建源代码发行版，请使用命令行导航到包含 setup.py 的目录，然后运行 python setup.py sdist 命令。
    运行 python setup.py bdist，或者对于Windows，使用 python setup.py bdist_wininst 来构建二进制分发。
    使用 python setup.py register，然后用 python setup.py sdist upload 来上传一个包。
    最后，用 python setup.py install 安装一个软件包。
"""

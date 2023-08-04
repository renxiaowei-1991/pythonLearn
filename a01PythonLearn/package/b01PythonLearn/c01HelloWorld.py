#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import sys

"""
    解释器

    关于脚本第一行的 #!/usr/bin/python 的解释，相信很多不熟悉 Linux 系统的同学需要普及这个知识，脚本语言的第一行，只对 Linux/Unix 用户适用，用来指定本脚本用什么解释器来执行。
    有这句的，加上执行权限后，可以直接用 ./ 执行，不然会出错，因为找不到 python 解释器。
    #!/usr/bin/python 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
    #!/usr/bin/env python 这种用法是为了防止操作系统用户没有将 python 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。
    #!/usr/bin/python 相当于写死了 python 路径。
    #!/usr/bin/env python 会去环境设置寻找 python 目录，可以增强代码的可移植性，推荐这种写法
"""

"""
    编码格式

    Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
    解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 # coding=utf-8 就行了
    注意：# coding=utf-8 的 = 号两边不要空格
    Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。
    注意：如果你使用编辑器，同时需要设置 py 文件存储的格式为 UTF-8，否则会出现类似以下错误信息
"""
print("Hello World!")
print("你好，世界！")

"""
    __future__ 包

    使用下一个版本支持的函数
"""
# from __future__ import print_function

"""
    标识符

    在 Python 里，标识符由字母、数字、下划线组成。
    在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
    Python 中的标识符是区分大小写的。
    以下划线开头的标识符是有特殊意义的。
        以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入
        以双下划线开头的 __foo 代表类的私有成员
        以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
    Python 可以同一行显示多条语句，方法是用分号 ;
    所有 Python 的关键字只包含小写字母
"""

"""
    行和缩进

    学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
    缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
    缩进不同会报错 

    IndentationError: unindent does not match any outer indentation level
"""

"""
    多行语句

    Python语句中一般以新行作为语句的结束符。
    1、但是我们可以使用斜杠（ \）将一行的语句分为多行显示
    2、语句中包含 [], {} 或 () 括号就不需要使用多行连接符
"""
item_one = "111"
item_two = '222'
item_three = '333'
total = item_one + \
        item_two + \
        item_three
print(total)
days = ['aa', 'bb', 'cc'
    , 'dd', 'ee']
print(days)

"""
    python 引号

    Python 可以使用引号( ' )、双引号( " )、三引号( ' ' ' 或 " " " ) 来表示字符串，引号的开始与结束必须是相同类型的。
    其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
"""
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落
包含了多个语句
"""

"""
    python 注释

    使用#，或者三引号( ' ' ' 或 " " " )
    使用#注释的时候，# 和被注释内容之间加个空格，否则忽悠警告
"""
# 第一个注释
"""
这是第二个注释
"""

""""
    Python空行

    函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
    空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构
"""

"""
    等待用户输入
    	raw_input  报错(已废弃)
    input()
    	input 输入的内容是字符串str，如果要对输入的内容进行计算。需要转换成int或其他的数值类型。
"""
# raw_input("按下enter键退出，其他任意键显示...\n")
num = int(input())

"""
    同一行显示多条语句

    Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
"""
a = 3
b = 4

"""
    print输出

    print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
"""
print(3, 4)

"""
    代码组

    多个语句构成代码组
    缩进相同的一组语句构成一个代码块，我们称之代码组。
    像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
    我们将首行及后面的代码组称为一个子句(clause)。
"""
if 4 > 3:
    print(4)
elif 4 > 5:
    print(5)
else:
    print(3)

"""
    命令行参数

    很多程序可以执行一些操作来查看一些基本信息，Python 可以使用 -h 参数查看各参数帮助信息
    python -h

    Python 提供了 getopt 模块来获取命令行参数。
    $ python test.py arg1 arg2 arg3

    Python 中也可以使用 sys 的 sys.argv 来获取命令行参数：
        sys.argv 是命令行参数列表。
        len(sys.argv) 是命令行参数个数。
    注：sys.argv[0] 表示脚本名。

    样例
        $ python test.py arg1 arg2 arg3
        参数个数为: 4 个参数。
        参数列表: ['test.py', 'arg1', 'arg2', 'arg3']

    getopt模块
"""

"""
    print函数可以使用end参数指定输出结束后的分隔符。默认是\n
    print("{}*{}={}".format(n, m, n*m), end=' ')
"""

print("参数个数为：", len(sys.argv), "个参数")
print("参数列表：", sys.argv)

# 命令行参数获取&操作
argvArray = sys.argv
print(argvArray)
# scriptName = argvArray[0]
# subArgvArray = argvArray[1:4]
scriptName,subArgvArray = argvArray[0],argvArray[1:4]
print(scriptName)
print(subArgvArray)
num = 0
while num < len(subArgvArray):
    print(subArgvArray[num])
    num += 1
    
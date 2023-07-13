#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string

"""
    字符串
        创建字符串，只需为变量分配一个值即可
        python 不支持单字符类型，单字符在python也是作为一个字符串使用
        [] 截取字符串
        +  链接字符串

    转义字符
        \   续行符(在行尾时)
        \\  反斜杠符号
        \'  单引号
        \b  退格(backspace)
        \n  换行
        \r  回车
        \t  横向制表符
        \f  换页

    字符串运算符
        +   字符串连接
        *   字符串重复
        []  通过索引获取字符串中字符
        [:] 截取字符串
        in  成员运算符
        not in 成员运算符
        %   格式字符串

    字符串格式化
        字符串格式化，最基本的用法是 将一个值插入到一个有字符串格式符 %s 的字符串中

        %c  格式化字符及其ACSII码
        %s  格式化字符串
        %d  格式化整数
        %u  格式化无符号整形
        %o  格式化无符号八进制数
        %x  格式化服务号十六进制数
        %X  格式化无符号十六进制数(大写)
        %f  格式化浮点数
        %e  用科学技术法格式化浮点数
        %E  作用同%e
        %g  %f 和 %e 的简写
        %G  %F 和 %E 的简写
        %p  用十六进制格式化变量的地址

        str.format() 格式化函数
            使用 {} 和 : 替换 %
            可以接受不限个数参数，位置可以不按照顺序

            参数可以按照顺序列出，也可以按照顺序按key值字典
            参数支持 列表、元组、字典
            列表和元组 替换的时候，列表和元组 变量名前加一个 *
            字典 替换的时候，字典 变量名前加两个 **
            如果不使用* **，则使用 0[] 的这种格式，也就是列表取值 、元组取值、字典取值的方式 引用

            "{} {}".format("hello","world")
            "{0} {1}".format("hello","world")
            "{1} {0} {1}".format("hello","world")

    三引号
        三引号允许一个字符串跨多行，可以包含各种特殊符号
        三引号让程序员从引号和特殊字符串的泥潭中解脱出来，保持一段字符串的 所见即所得

    字符串函数
        string.capitalize()
            把字符串的第一个字符大写
        string.center(width)
            返回一个新字符串，把原字符串居中，并使用空格填充至长度width
        string.count(str,beg=0,end=len(string))
            返回str在string里面出现的次数，如果beg或者end指定，则返回指定范围内str出现的次数
        string.decode(encoding='UTF-8',errors='strict') 
            以encoding指定的编码格式解码string，如果出错默认报一个ValueError的异常，
            除非errors指定的是'ignore' 或者 'replace'
        string.encode(encoding='UTF-8',errors='strict')
            已encoding指定的编码格式编码string，如果出错默认报一个ValueError的异常，
            除非errors指定的是'ignore' 或者 'replace'
        string.find(str,beg=0,end=len(string))
            检测str是否包含在string中，如果beg和end指定范围，则检查范围按照指定范围，
            如果包含，返回开始的索引值，否则返回-1
        string.index(str,beg=0,end=len(string))
            等同于string.find()，只不过如果没有找到，会报错
        string.format()
            字符串格式化
        string.join(seq)
            以string作为分隔符，将seq中所以元素(的字符串表示)合并为一个新的字符串
        string.lower()
            大写转小写
        string.upper()
            小写转大写
        string.replace(str1,str2,num=string.count(str1))
            把string中的str1替换成str2，如果num指定，则替换次数不超过num次
        string.split(str="",num=string.count(str))
            已str为分隔符切片string，如果num有指定值，则仅分割num+1个字符串
        string.lstrip()
            截取string左边的空格
        string.rstrip()
            删除string字符串末尾的空格
        string.strip()
            lstrip() + rstrip()
        string.zlill(2)
            补齐两位(2->02),用于数值月份转字符串月份
        string.rjust(2,"0")
            等价于string.zlill(2)
            不过rjust可以指定用于补充的字符
            补齐两位(2->02),用于数值月份转字符串月份

"""

print("字符串练习：")
a = "Hello"
b = "python"
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1]输出结果：", a[1])
print("a[1:4]输出结果：", a[1:4])

if 'H' in a:
    print('H在变量a中')
else:
    print('H不在变量a中')

if 'H' not in a:
    print("H不在变量a中")
else:
    print("H在变量a中")

print("字符串格式化练习：")
print("My name is %s and weight is %d kg!" % ('renxiaowei', 75))

print("格式化函数format练习")
print("{} {}".format("hello", "world"))
print("{0} {1}".format("hello", "world"))
print("{1} {0} {1}".format("hello", "world"))
print("{hello} {world} {hello}".format(hello="hello", world="world"))

print("格式化函数format练习:列表")
list = ["hello", "world"]
print("{1} {0} {1}".format(*list))
print("{0[1]} {0[0]} {0[1]}".format(list))

print("格式化函数format练习:元组")
list = ("hello", "world")
print("{1} {0} {1}".format(*list))
print("{0[1]} {0[0]} {0[1]}".format(list))

print("格式化函数format练习:字典")
dict = {'hello': "hello", 'world': "world"}
print("{hello} {world} {hello}".format(**dict))
print("{0[hello]} {0[world]} {0[hello]}".format(dict))


# 字符串在创建的时候就需要进行格式化，不能在创建好后再格式化，不生效
tableName = 'dmf_dev.renxiaowei_20230622_tmp_01'
tx_date = '2023-06-22'
filter = "code = 11"
sql01 = """
    select *
    from {tableName} a1
    where dt = '{tx_date}'
      and {filter}
""".format(tableName=tableName, tx_date=tx_date, filter=filter)
print(sql01)

listA = ['dmf_dev.renxiaowei_20230622_tmp_01', '2023-06-22', "code = 11"]
tupleA = ('dmf_dev.renxiaowei_20230622_tmp_01', '2023-06-22', "code = 11")
dictA = {'tableName': tableName, 'tx_date': tx_date, 'filter': filter}

sql02 = """
    select *
    from {tableName} a1
    where dt = '{tx_date}'
      and {filter}
""".format(**dictA)

sql03 = """
    select *
    from {tableName} a1
    where dt = '{tx_date}'
      and {filter}
""".format(**dictA)

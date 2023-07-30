#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import re

"""
正则表达式
    正则表达式是一种文本模式，包含普通字符(例如，a到z之间的字母）和特殊字符(称为"元字符")。可以用来描述和匹配字符串的特定模式
    正则表达式是一种用于模式匹配和搜索文本的工具
    正则表达式提供了一种灵活且强大的方式来查找、替换、验证、提取文本数据
    
正则表达式的模式
    字符匹配
        普通字符：例如字母、数字、空格等，可以直接匹配他们自身。例如匹配字母"a"将匹配到文本中"a"字符
            普通字符包含没有显示指定为元字符的所有可打印和不可打印字符。这包括所有大写和小写字母、所有数字、所有标点符号和其它一些符号
            a-z : 所有小写字母
            A-Z : 所有大写字母
            0-9 : 所有数字
            
        
        元字符：例如 \d、\w、\s 等，用于匹配特定类型的字符，如 数字、字母、空白字符等。
            \d : 匹配任意数字字符
            \D : 匹配任意非数字字符。等价与 [^0-9]
            \w : 匹配任意字母数字字符(字母、数字、下划线，等价于[a-zA-Z0-9_])
            \W : 匹配任意非字母数字字符(匹配非字母、数字、下划线，等价于[^a-zA-Z0-9_])
            . : 匹配任意字符(除了换行符)
            
            非打印字符：
                \cx : 匹配由x指明的控制符。
                    例如： \cM 匹配一个Control-M或者回车符。x的值必须为A-Z或a-z之一。否则，将c视为一个原义的"c"字符
                \f : 匹配一个换页符。等价于 \x0c 和 \cL
                \n : 匹配一个换行符。等价于 \x0a 和 \cJ
                \r : 匹配一个回车符。等价域 \x0d 和 \cM
                \t : 匹配一个制表符。等价于 \x09 和 \cI
                \v : 匹配一个垂直制表符。等价于 \x0b 和 \cK
                \s : 匹配所有空白符，包括空格、制表符、换页符等。等价于[\f\n\r\t\v]。Unicode正则表达式会匹配全角空格符
                \S : 非空白符，不包含换行。等价于[^\f\n\r\t\v]
                
                
    字符类：用方括号[ ] 包围的字符集合，用于匹配方括号内的任意一个字符。
        [ ] : 匹配括号内的任意一个字符。例如,[abc] 匹配 "a"、"b"或"c" 
        [^ ] : 匹配除了括号内的字符以外的任意一个字符。例如, [^abc] 匹配除了字符"a"、"b"或"c" 以外的任意字符
    
    量词(限定符)：例如 {n} 、 {n,} 、 {n,m} 等，用于指定匹配的次数或范围
        * : 匹配前面的模式零次或多次(贪婪匹配)
        + : 匹配前面的模式一次或多次(贪婪匹配)
        ? : 匹配前面的模式零次或一次(非贪婪匹配)
            * 和 + 都是贪婪匹配，会尽可能多的匹配文章。只有在他们的后面加上一个? 就可以实现非贪婪或最小匹配
            [0-9]* : 匹配0-9任意多次
                文本 : <h1>RUNOOB-菜鸟教程</h1>
                结果 : <h1>RUNOOB-菜鸟教程</h1>
            [0-9]*? : 匹配0-9，匹配到一次就结束
                文本 : <h1>RUNOOB-菜鸟教程</h1>
                结果 : <h1>
                    加了? 就匹配满足规则的最小的结果
                    不加? 就匹配满足规则的最大的结果
        {n} : 匹配前面的模式正好n次
        {n,} : 匹配前面的模式至少n次(相当于{n,m}中不指定m的限定)
        {n,m} : 匹配前面的模式至少n次，且不超过m次
        { } : 标记限定符表达式的开始。
    边界符号(定位符)：例如 ^ 、 $ 、 \b 、 \B 等，用于匹配字符串的开头、结尾或单词边界位置
        ^ : 匹配字符串的开头(一行文本的开头)
        $ : 匹配字符串的结尾(一行文本的结尾)
        \b : 匹配单词边界(字符与空白符(\s)之间的位置)
            如果它位于要匹配的字符串的开始，它在单词的开始处查找匹配项。如果它位于字符串的结尾，它在单词的结尾处查找匹配项。
            "\bCha"
                匹配以Cha开头的单词
            "ter\b"
                匹配以ter结尾的单词
        \B : 匹配非单词边界
            匹配不是单词边界的结果
            "\Bapt"
                匹配Chapter中的字符串apt。不匹配aptitube中的字符串apt
        \A : 匹配字符串开始
        \Z : 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
        \z : 匹配字符串结束
        \G : 匹配最后匹配完成的位置
    分组、选择和捕获
        (pattern) : 用于分组和捕获子表达式。标记一个子表达式的开始和结束位置。
            匹配pattern，并且获取
            用圆括号()将所有选择项括起来，响铃的选择项之间用 | 分割
            使用圆括号会有一个副作用，使相关的匹配会被缓存，可以使用 ?: 放在第一个选项消除这种副作用
        (?:pattern) : 用于分组但不捕获子表达式。匹配pattern，但是不获取
        非捕获元(非获取匹配，匹配结果不获取)
            ?:
            ?= 正向预查，在任何开始匹配圆括号的正则表达式模式的位置来匹配搜索字符串
                exp1(?=exp2]):查找后面是exp2的exp1
                runoob(?=[\b+]):查找后面是任意位数字前面的runoob
            ?<=
                (?<=exp2)exp1:查找前面是exp2的exp1
                (?<=[\b+])runoob:查找前面是任意位数字的runoob
            ?! 反向预查，在任何开始不匹配该正则表达式模式的位置来匹配搜索字符串
                exp1(?!exp2]):查找后面不是exp2的exp1
                runoob(?![\b+]):查找后面不是任意位数字的runoob
            ?<!
                (?<!exp2)exp1:查找前面不是exp2的exp1
                (?<![\b+])runoob:查找前面不是任意位数字的runoob
        \1...\9 : 匹配第n个分组的内容
        \10 : 匹配第n个分组的内容。
    特殊字符
        \ : 转义字符，用于匹配特殊字符本身
        . : 匹配任意字符(除了换行符)
        | : 用于指定多个模式的选择。指明两项之间的一个选择。
        
匹配符优先级
    转义符 \ 
    限定符 (),(?:),(?=),[] 
    定位符 *,+,?,{n},{n,},{n,m} 
    字符   ^,$,\任何元字符，任何字符 定位点和序列(位置和顺序)
    选择符 | 
    
            
    
正则表达式作用
    测试字符串内的模式
        可以测试输入字符串，以查看字符串内是否出现电话号码模式或行用卡模型。称为数据验证
    替换文本
        可以使用正则表达式来识别文本中的特定文本，完全删除该文本或者使用其它文本替换它
    用于模式匹配从字符串中提取子字符串
        可以查找文档内输入域内特定的文本


常见匹配样例：
    用户名：
        "^[a-z0-9_-]{3-15}$"
        写用户注册表单时，只允许用户名包含字符、数字、下划线和连接字符-，并设置用户名长度3-15位，可以使用正则表达式匹配
    
    邮箱：
        ***@***.***
        \b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b
            \b 单词边界
            [\w.%+-]+
                \w  [a-zA-Z0-9_]
                .   匹配任意字符(除了换行符)
                +   普通字符
                -   普通字符
                +   匹配1次或多次
            @ 普通字符
            [\w.-]+
                \w  [a-zA-Z0-9_]
                .   匹配任意字符(除了换行符)
                -   普通字符
                +   匹配1次或多次
            \. 匹配 .
            [a-zA-Z]{2,6}
                匹配a-zA-Z，2次到6次
            \b 匹配单词边界
    

"""

"""
https://www.runoob.com/python3/python3-reg-expressions.html

re模块函数
    正则表达式是一个特殊的字符序列，能方便的检查一个字符串是否与某种模式匹配
    re模块 使Python语音拥有了全部的正则表达式功能
    compile函数 根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换
    re模块 也提供了与这些方法功能完全一致的函数。这些函数使用一个模式字符串做为它们的第一个参数
    
    标志位(修饰符)
        正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
        修饰符是一个可选标志。
        多个标志可以通过按位OR(|)来指定。
            例如： re.I|re.M
        
        re.I : 使匹配对大小写不敏感
        re.L : 做本地化识别匹配
        re.M : 多行匹配，影响^和$
        re.S : 使 . 匹配包括换行在内的所有字符
        re.U : 根据Unicode字符集解析字符。这个标志影响 \w,\W,\b.\B
        re.X : 通过给予更灵活的格式以便将正则表达式写得更易于理解。

    re.match(pattern, string, flags=0)
        re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
        匹配成功返回匹配的对象，否则返回none
        参数说明：
            pattern  匹配的正则表达式
            string   要匹配的字符串
            flags    标志位(修饰符)，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
        
        
        可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
            group(num=0) 
                匹配的整个表达式的字符串，group() 可以一次输入多个组号，返回一个包含这些组号所对应值的元组
            groups()
                返回一个包含所有小组字符串的元组，从1到所含的小组号
            span() 
                在起始位置匹配
                默认不在起始位置匹配
                
                
    re.search(pattern, string, flags=0)
        匹配成功，返回一个匹配的对象，否则返回None
        参数说明：
            pattern  匹配的正则表达式
            string   要匹配的字符串
            flags    标志位(修饰符)，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
        可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
        
    re.match & re.search:
        re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配识别，返回None
        re.search 匹配整个字符串，直到找到一个匹配
        
    re.sub(patten, repl, string, count=0, flags=0)
        替换字符串中的匹配项
        参数说明：
            pattern: 正则中的模式字符串
            repl: 替换的字符串，也可为一个函数
            string: 要被查找替换的原始字符串
            count: 模式匹配后替换的最大次数，默认0表示替换所有的匹配
            flags    标志位(修饰符)，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
    
    re.compile(pattern[, flags])
        compile函数用于编译正则表达式，生成一个正则表达式(Pattern)对象，供match()和search()这两个函数使用
        参数说明：
            pattern: 一个字符串形式的正则表达式
            flags    标志位(修饰符)，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
        
        注意：
            compile提取编译好正则表达式，后续多次使用性能更好
        
    
    re.findall
        在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
        语法：
            re.findall(pattern, string, flags=0)
            pattern.findall(string,[, pos[, endpos]])
        
        参数说明：
            pattern: 匹配模式
            string: 待匹配的字符串
            pos: 可选参数，指定字符串的起始位置，默认为0
            endpos: 可选参数，指定字符串的结束位置，默认为字符串的长度
            
        
        注意：
            match和search是匹配一次，findall匹配所有
    
    re.finditer(pattern, string, flags=0)
        和findall类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
        参数说明：
            pattern  匹配的正则表达式
            string   要匹配的字符串
            flags    标志位(修饰符)，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
    
    re.split(pattern, string[, maxsplit=0, flags=0])
        split方法按照能够匹配的子串将字符串分割后返回列表
        参数说明：
            pattern  匹配的正则表达式
            string   要匹配的字符串
            maxsplit: 分割次数，maxsplit=-1 分割一次，默认为0，不限制次数
            flags    标志位(修饰符)，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等。
    
    正则表达式对象
        re.RegexObject
            re.compile()返回RegexObject对象
        re.MatchObject
            group() 返回被RE匹配的字符串
                start() 返回匹配开始的位置
                end() 返回匹配结束的位置
                span() 返回一个元组包含匹配(开始, 结束)的位置
    
    正则表达式模式(特殊部分)
        (re)
        (?imx)
        (?-imx)
        (?:re)
        (?imx:re)
        (?-imx:re)
        (?#)
        (?=re)
        (?!re)
        (?>re)
        (?<re)
        (?<=re)
    
    
    公用方法：
        注意：
            下面这些方法都是可以基于子串进行使用的。
            子串：通过匹配模式中( )方式匹配出来的多个子结果
            正则表达式通常都包含反斜杠，所有最好使用原始字符串来表示。
            模式原始(r"\t", 等价于"\\t")匹配想要特殊字符
            r"\t", 等价于"\\t"
        
        匹配模式：
            一组()表示一个匹配模式，() () ，表示两个匹配模式。
            re.match(从头匹配): 取一组匹配结果，匹配模式匹配到的一个结果中的多个子串
            re.search(整体匹配): 取一组匹配结果，匹配模式匹配到的一个结果中的多个子串
            re.compile(正则对象): 方便 match和search使用
            通过()将匹配结果分组后，可以通过\1...\9 \10，匹配第n个组的内容
        
        匹配结果
            元组(一个匹配结果的多个匹配模式结果)：多个匹配模式的结果需要通过元组的方式存放。表示的是一个匹配结果
            列表(单模式&多模式的多个匹配结果)：单模式，或者多个匹配模式作为一组匹配，匹配到的多个结果需要放到列表里面。
            样例：
                [('123', 'google'), ('456', 'www')]
            
            re.findall: 取多个匹配结果。每个匹配结果可能包含多个匹配模式匹配到的多个子串
        
        group([group1, ...])
            匹配结果
            用于获取一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用group()或group(0)
            group表示想要获取的子串
            这里说的匹配子串是表示在正则表达式模式中，用( )限定的匹配子串
            例如：
                line = "Cats are smarter than dogs"
                # (.*) 限定出来的是第一个子串，使用group(1)获取
                # (.*?) 限定出来的是第二个子串，使用group(2)获取
                matchObj = re. match(r"(.*) are (.*?) .*", line)
                matchObj.group(0)
                matchObj.group(1)
                matchObj.group(2)
        groups()
            以元组的形式获取所有的匹配子串，就是group()样例中，用(.*)和(.*?)限定出来的匹配子串
            包括两个子串：
                matchObj.group(1)
                matchObj.group(2)
                type(matchObj.groups()) # tuple
        start([group])
            匹配结果开始位置
            用于获取分组匹配的子串在整个字符串中的起始位置(子串第一个字符的索引)，参数默认为0
            group表示想要获取的子串
        end([group])
            匹配结果结束位置
            用于获取分组匹配的子串在整个字符串中的结束位置(子串最后一个字符的索引+1)，参数默认为0
            group表示想要获取的子串
        span([group])
            子串索引范围
            返回(start(group), end(group))
            group表示想要获取的子串
            span(3, 10)
                正则匹配结果中，span(3, 10) 里面的数字表示的是匹配结果在原字符串中的开始位置和结束位置的索引位
"""


def re_match():
    print("第一次匹配")
    string = "www.runoob.com"
    print("返回结果是一个match对象，可以通过函数进行操作：", re.match("www", string))
    print(re.match("www", string).span())
    print(re.match("com", string))
    print("获取匹配到的整个结果：", re.match("www", string).group())
    print("获取匹配到的第一个结果：", re.match("www", string).group(0))
    print(re.match("www", string).groups())

    print("第二次匹配")
    string = "www.runoob.com www.runoob.com"
    print("返回结果是一个match对象，可以通过函数进行操作：", re.match("www", string))
    print(re.match("www", string).span())
    print(re.match("com", string))
    print("获取匹配到的整个结果：", re.match("www", string).group())
    print("获取匹配到的第一个结果：", re.match("www", string).group(0))
    print(re.match("www", string).groups())

    print("第三次匹配")
    line = "Cats are smarter than dogs"
    # 正则表达式中
    # (.*) 表示第一个匹配子串。匹配子串用()限定
    # (.*?) 表示第二个匹配字符串。
    matchObj = re.match(r"(.*) are (.*?) .*", line)
    print(matchObj)
    if matchObj:
        print("子串元组(groups()): ")
        print("matchObj.groups(): ", matchObj.groups(), ", 类型是：", type(matchObj.groups()))

        print("子串演示()(整个结果字符串)：")
        print("mathcObj.group(): ", matchObj.group())
        print("matchObj.start(): ", matchObj.start())
        print("matchObj.end(): ", matchObj.end())
        print("matchObj.span(): ", matchObj.span())

        print("子串演示(0)(整个结果字符串)：")
        print("mathcObj.group(0): ", matchObj.group(0))
        print("matchObj.start(0): ", matchObj.start(0))
        print("matchObj.end(0): ", matchObj.end(0))
        print("matchObj.span(0): ", matchObj.span(0))

        print("子串演示(1)(第一个子串)：")
        print("mathcObj.group(1): ", matchObj.group(1))
        print("matchObj.start(1): ", matchObj.start(1))
        print("matchObj.end(1): ", matchObj.end(1))
        print("matchObj.span(1): ", matchObj.span(1))

        print("子串演示(2)(第二个子串)：")
        print("mathcObj.group(2): ", matchObj.group(2))
        print("matchObj.start(2): ", matchObj.start(2))
        print("matchObj.end(2): ", matchObj.end(2))
        print("matchObj.span(2): ", matchObj.span(2))

    else:
        print("No match!")
    return


def re_search():
    print("第一次匹配")
    line = "www.runoob.com"
    print(re.search("www", line).span())
    print(re.search("com", line).span())
    print(re.search("www", line))
    print(re.search("com", line))
    print(re.search("www", line).group())
    print(re.search("com", line).group())
    return


# 用于re.sub匹配后处理
def double(matched):
    value = int(matched.group("value"))
    return str(value * 2)


def re_sub():
    phone = "2004-959-959 # 这是一个电话号码"

    # 删除注释
    num = re.sub(r"#.*$", "", phone)
    print(f"电话号码: {num}")

    # 移除非数字的内容
    num = re.sub(r"\D", "", phone)
    print(f"电话号码: {num}")

    # repl参数是一个函数
    # 将字符串中匹配的数字乘以2
    string_a = "A23G4HFD567"
    print(re.sub(r"(?P<value>\d+)", double, string_a))
    return


def re_compile():
    print("compile(第一组)")
    pattern = re.compile(r"\d+")
    m = pattern.match("one12twothree34four")
    print(m)
    m = pattern.match("one12twothree34four", 2, 10)  # 从索引2开始匹配(从'e'的位置开始匹配)，没有匹配结果
    print(m)
    m = pattern.match("one12twothree34four", 3, 10)  # 从索引3开始匹配(从'1'的位置开始匹配)，由匹配结果
    print(m)
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

    print("compile(第二组)")
    pattern = re.compile(r"([a-z]+) ([a-z]+) ([a-z]+)", re.I)  # re.I: 忽略大小写
    m = pattern.match("Hello World Wide Web")
    print(m.groups())
    m = pattern.search("Hello World Wide Web")
    print(m.groups())
    return


def re_findall():
    result1 = re.findall(r"\d+", "runoob 123 google 456")
    pattern = re.compile(r"\d+")
    result2 = pattern.findall("runoob 123 google 456")
    result3 = pattern.findall("runoob123google456", 0, 10)
    pattern = re.compile(r"(\d+) (\w+)")
    result4 = pattern.findall("runoob 123 google 456 www")
    result5 = pattern.findall("runoob123google456", 0, 10)
    pattern = re.compile(r"(\d+|\w+)")
    result6 = pattern.findall("runoob 123 google 456 www")
    result7 = pattern.findall("runoob123google456", 0, 10)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)
    return


def re_finditer():
    result1 = re.finditer(r"\d+", "12a32bc43jf3")
    for r in result1:
        print(r)
    return


def re_split():
    str1 = "runoob 123 google 456 www"
    str2 = "runoob123google456"
    result1 = re.split(r" ", str1)
    print(result1)
    result2 = re.split(r"\d+", str1)
    print(result2)
    result3 = re.split(r" ", str1, maxsplit=1)
    print(result3)
    return


def re_all():
    str1 = "runoob 123 google 456 www"
    str2 = "runoob123google456"
    pattern1 = r"\d+"
    pattern2 = r"\w+"
    pattern3 = r"(\d+) (\w+)"
    pattern4 = r"(\d+|\w+)"
    result1 = re.match(pattern3, str1, flags=0)
    print(result1)
    result2 = re.search(pattern3, str1, flags=0)
    print(result2)
    print(result2.group(1))
    print(result2.group(2))
    result3 = re.compile(pattern3, flags=0)
    print(result3.match(str1))
    print(result3.search(str1))
    result4 = re.findall(pattern3, str1, flags=0)
    print(result4)
    result5 = re.finditer(pattern3, str1, flags=0)
    print(list(result5))

    # print(111)
    # for r in result5:
    #     print(r.group(1))
    #     print(r.group(2))
    # print(r)

    print(type(result3))
    print(type(result2.group()))

    return


def date_is_right(date: str):
    """
    判断输入的字符串是否是10为日期格式：YYYY-MM-DD
    :param date: 字符串格式日期
    :return: 返回判断结果
    """
    result = False
    pattern = r"\d{4}-\d{2}-\d{2}"
    # 如果有匹配结果，会返回re.match对象，如果没有匹配结果，返回None
    match_str = re.match(pattern, date, flags=0)
    # result = True if match_str is not None else False
    # match_str is not None 就是一个boolean值
    result = match_str is not None
    # print(match_str)
    return result


def get_phone_num(string: str):
    """
    提取文本中的电话号码
    电话号码模式：1开头，长度为11位的数值串
    :param string:
    :return: 返回提取到的电话号码的列表
    """
    pattern = r"1\d{10}"
    # re.findall可以搜索文本中的所有匹配的模式
    result = re.findall(pattern, string, flags=0)
    return result


def get_mailbox_num(string: str):
    """
    从文本中提取邮箱列表
    邮箱匹配模式：多位字母数字下划线中划线@多位字母数字.2~4位字母
        \w: [a-zA-Z0-9_](经过测试，还能匹配中文)
        *: 0或多位
        +: 1或多位
        .: 匹配任意字符(除了换行符)(如果匹配.本身，需要转义)
        {2,4}: 匹配长度2-4位，不能写成{2-4}和{2, 4}
    compile提取编译好正则表达式，后续多次使用性能更好
    :param string:
    :return:
    """
    pattern = r"[0-9a-zA-Z_-]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,4}"
    result = re.findall(pattern, string, flags=0)
    # pattern = re.compile(r"[0-9a-zA-Z_-]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,4}", flags=0)
    # result = pattern.findall(string)
    return result


def content_hide(string: str):
    """
    替换文本中不允许使用的词
    :param string:
    :return: 返回替换以后的结果
    """
    pattern = re.compile(r"(最好|最低|绝对)", flags=0)
    result = pattern.sub("***", string)
    # pattern = r"(最好|最低|绝对)"
    # result = re.sub(pattern, "***", string)
    return result


def handle_phone_num(string: str):
    """
    将文本中电话号码加密
    电话号码模式：1开头，长度为11位的数值串
    将匹配结果替换成 \1******\3，\1表示第一组匹配模式匹配结果,\3表示第三组匹配模式匹配结果
    :param string:
    :return:
    """
    pattern = re.compile(r"(1\d)(\d{7})(\d{2})", flags=0)
    result = pattern.search(string)
    # print(result)
    # print(result.group(1))
    # print(result.group(2))
    # print(result.group(3))
    # 将匹配结果替换成 \1******\3，\1表示第一组匹配模式匹配结果,\3表示第三组匹配模式匹配结果
    result = pattern.sub(r"\1******\3", string)
    return result


# re_match()
# re_search()
# re_sub()
# re_compile()
# re_findall()
# re_finditer()
# re_split()
# re_all()
print("2023-07-29", date_is_right("2023-07-29"))
print("202-05-20", date_is_right("202-05-20"))
print("2021/05-20", date_is_right("2021/05-20"))
print("20230729", date_is_right("20230729"))
print("20a10729", date_is_right("20a10729"))

text = "白日依19989881888山尽，黄河入45645546468798987海流。" \
       "欲穷12345千里目，更上15619292345一层楼。"
print(get_phone_num(text))

content = """
寻隐者12345@qq.com不遇
朝代：唐asdf12dsa#abc.com代
作python666@163.cn者：贾岛
松下问童子，言师python-abc@163com采药去。
只在python_ant-666@sina.net此山中，云深不知处。
"""
print(get_mailbox_num(content))

content = "这个商品很好，质量最好，用起来很不错，并且价格最低，绝对的物美价廉"
print(content_hide(content))


content = """
白日依19989881888山尽，黄河入45645546468798987海流。
欲穷12345千里目，更上15619292345一层楼。
"""
print(handle_phone_num(content))
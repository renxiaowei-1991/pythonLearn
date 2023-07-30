#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


def date_is_right(date: str):
    """
    判断输入的字符串是否是10为日期格式：YYYY-MM-DD
    日期模式：YYYY-MM-DD
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
    print(result)
    # print(result.group(1))
    # print(result.group(2))
    # print(result.group(3))
    # 将匹配结果替换成 \1******\3，\1表示第一组匹配模式匹配结果,\3表示第三组匹配模式匹配结果
    result = pattern.sub(r"\1******\3", string)
    return result


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

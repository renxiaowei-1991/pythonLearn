#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pprint import pprint
import json

"""
json
    json是封装的，多语言可以识别的格式。用于进行系统交互。
    本身是一个字符串。只不过这个字符串里面的内容是按照字典及多级字典的格式组织的

json.dumps: 可以将对象变成json
    indent: 缩进参数。使json字符串样式更加缩进美观
        如果不加indent，转换后的字符串结果就是一行，没有换行，没有缩进。
        如果加了indent，转换后的字符串结果会按json格式换行，并且按照指定的宽度缩进

json.loads: 将json格式内容转换成字典
"""
BASE_PATH = "D:\\02helloWorld\\03Python\\a01pythonLearn\\"

DATA = {"employees": [{"firstName": "John", "lastName": "Doe"},
                      {"firstName": "Anna", "lastName": "Smith"},
                      {"firstName": "Peter", "lastName": "Jones"}],
        "owners": [{"firstName": "Jack", "lastName": "Petter"},
                   {"firstName": "Jessy", "lastName": "Petter"}]}


def json_demo():
    """
    将字典使用json.dumps转换成json格式字符串。按指定缩进写入文件中
    :return:
    """
    file_path = "file\\p060.json"
    pprint(json.dumps(DATA))
    pprint(json.dumps(DATA, indent=2)) # 缩进两个字符
    pprint(type(json.dumps(DATA)))
    with open(BASE_PATH + file_path, "w+", encoding="utf-8") as f:
        try:
            f.write(json.dumps(DATA, indent=2))
        except BaseException as be:
            print(be)
        finally:
            f.close()
    return True


def json_re_demo():
    """
    从指定文件读取json格式字符串，使用json.loads转换成字典。使用pprint进行格式化输出
    :return:
    """
    file_path = "file\\p060.json"
    with open(BASE_PATH + file_path, "r+", encoding="utf-8") as f:
        try:
            sr = f.read()
            print(sr)
            pprint(json.loads(sr))
            print(type(json.loads(sr)))
        except BaseException as be:
            print(be)
        finally:
            f.close()
    return True


# json_demo()
# json_re_demo()
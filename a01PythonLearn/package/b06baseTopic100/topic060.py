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
"""
BASE_PATH = "D:\\02helloWorld\\03Python\\a01pythonLearn\\"

DATA = {"employees": [{"firstName": "John", "lastName": "Doe"},
                      {"firstName": "Anna", "lastName": "Smith"},
                      {"firstName": "Peter", "lastName": "Jones"}],
        "owners": [{"firstName": "Jack", "lastName": "Petter"},
                   {"firstName": "Jessy", "lastName": "Petter"}]}


def json_demo():
    file_path = "file\\p060.json"
    pprint(json.dumps(DATA))
    pprint(json.dumps(DATA, indent=2))
    pprint(type(json.dumps(DATA)))
    with open(BASE_PATH + file_path, "w+", encoding="utf-8") as f:
        try:
            f.write(json.dumps(DATA, indent=2))
            # f.write(json.dumps(DATA))
        except BaseException as be:
            print(be)
        finally:
            f.close()


if __name__ == "__main__":
    json_demo()

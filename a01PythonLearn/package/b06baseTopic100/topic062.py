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

def json_read_demo():
    """
    从文件读取json格式字符串，转换成dict，添加内容，返回结果
    """
    file_path = "file\\p060.json"
    sr: str = ""
    with open(BASE_PATH + file_path, "r+", encoding="utf-8") as f:
        try:
            sr = f.read()
        except BaseException as be:
            print(be)
        finally:
            f.close()
    # print(sr)
    # 转换成dict
    sr_json = json.loads(sr)
    pprint(sr_json)
    # print(type(sr_json))
    sr_json["employees"].append({'firstName': 'Albert', 'lastName': 'Bert'})
    pprint(sr_json)
    return sr_json


def json_write_demo():
    file_path = "file\\p062.json"
    sr_json = json_read_demo()
    # pprint(json.dumps(sr_json))
    # pprint(json.dumps(sr_json, indent=2))
    # pprint(type(json.dumps(sr_json)))
    with open(BASE_PATH + file_path, "w+", encoding="utf-8") as f:
        try:
            f.write(json.dumps(sr_json, indent=2))
            # f.write(json.dumps(DATA))
        except BaseException as be:
            print(be)
        finally:
            f.close()


if __name__ == "__main__":
    json_write_demo()
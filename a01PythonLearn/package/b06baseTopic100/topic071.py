#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

DATA = {"apple": "苹果", "orange": "桔子", "banana": "香蕉"}
BASE_PATH = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\"

def load_dict(file_path: str):
    """
    读取指定路径的文件，按照json格式转换成dict，并且返回
    :param file_path:
    :return:
    """
    with open(file_path, "r+", encoding="utf-8") as f:
        try:
            return json.loads(f.read())
        except BaseException as be:
            print(f"异常：{be}")
            return None


def translate_demo(word: str):
    """
    根据字典进行翻译：忽略大小写
    :return:
    """
    re = load_dict(BASE_PATH + "fruitsDict.json")[word.lower()]
    return re


if __name__ == "__main__":
    """查找在字典中存在的值，错误的话继续，直到找到值"""
    rs = ""
    fruits = input("Enter word: ")
    while True:
        try:
            rs = translate_demo(fruits)
            if rs is not None:
                break
        except BaseException as be:
            fruits = input("单词不在词典中，请重新输入: ")
    print(rs)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

DATA = {"apple": "苹果", "orange": "桔子", "banana": "香蕉"}


def translate_demo(word):
    """
    根据字典进行翻译
    :return:
    """
    re = DATA[word]
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

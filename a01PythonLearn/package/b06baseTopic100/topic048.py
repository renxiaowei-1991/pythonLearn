#!/usr/bin/env python
# coding=utf-8


def char_count(word):
    """
    以任何一个英文单词作为入参，返回英文单词的字符数
    :param word:
    :return:
    """
    return len(word)


def word_count(str_in):
    """
    以任何一个英文字符串作为入参，返回英文单词的数目
    :param str_in:
    :return:
    """
    # split默认可以使用空格进行分割，如果要使用其它符号分割，需要进行指定split(" ")
    return len(str_in.split())


print(char_count(input("Enter a english word: ")))
print(word_count(input("Enter a string: ")))

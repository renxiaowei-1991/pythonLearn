#!/usr/bin/env python
# coding:utf-8

import file
import re


def count_file_word(file_path_in, separator=" "):
    """
    统计文件单词数(用多种分隔符拆分字符串，多种分隔符之间用|分割)
    :param file_path_in:
    :return:
    """
    count = 0
    try:
        file01 = open(file_path_in, "r+", encoding="utf-8")

        for line in file01.readlines():
            if len(separator) == 1:
                count += len(line.split(separator))
            else:
                count += len(re.split(separator, line))
    except BaseException as be:
        print(f"文件读取异常，异常原因：{be}")
    else:
        print("文件读取成功！")
    finally:
        if not file01.closed:
            file01.close()
    return count


if __name__ == "__main__":
    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\file04.txt"
    print(count_file_word(file_path, r"\|,| "))
    print(r"hello \n world")

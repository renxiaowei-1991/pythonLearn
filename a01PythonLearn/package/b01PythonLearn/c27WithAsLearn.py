#!/usr/bin/env python
# coding=utf-8

import os
import sys
import file

"""
with ... as ...:
    with as 的用法相当于oracle里面的 with ... as ...的用法
    相当于把一个对象起个别名，在后面可以重复使用。
    
注意：
    用with的方式打开的文件，不用主动使用close()关闭，会自动关闭
"""


def count_words(file_path_in):
    """
    统计输入参数文件中单词个数
    :param file_path_in:
    :return:
    """
    count = 0
    with open(file_path_in, "r+", encoding="utf-8") as file:
        try:
            for line in file.readlines():
                count += len(line.split())
        except BaseException as be:
            print(f"文件读取异常，异常原因：{be}")
        else:
            print("文件读取完成！")
        finally:
            if not file.closed:
                file.close()
    return count


if __name__ == "__main__":
    # print(os.getcwd())
    # print(dir(sys))
    # print(sys.__doc__)
    # print(sys.path)
    # print(sys.path.append(""))
    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\file04.txt"
    print(count_words(file_path))

#!/usr/bin/env python
# coding=utf-8

import file


def count_file_word(file_path_in):
    """
    统计输入参数文件中单词个数
    :param file_path_in:
    :return:
    """
    try:
        file01 = open(file_path_in, "r+", encoding="utf-8")
        count = 0
        for line in file01.readlines():
            count += len(line.split())
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
    rs_count = count_file_word(file_path)
    print(rs_count)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import file


class WordCount:
    def __init__(self):
        pass

    @staticmethod
    def count_file_word(file_path_in, separator=" "):
        """
        统计输入参数文件中单词个数(使用默认分隔符)
        :param separator:可以指定分隔符，默认是空格，如果指定多个分隔符(多个分隔符之间使用|进行分割)，使用re.split方法进行分割
        :param file_path_in:传入统计的文件
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


# 测试脚本
# file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\file04.txt"
# print(WordCount.count_file_word(file_path, r"\|,| "))

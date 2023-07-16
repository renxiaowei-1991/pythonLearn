#!/usr/bin/env python
# coding=utf-8

import string
import file


def create_file(file_path_in):
    """
    将所有小写字母写入文件，每行一个
    :param file_path_in:
    :return:
    """
    with open(file_path_in, "w+", encoding="utf-8") as file01:
        try:
            for i in string.ascii_lowercase:
                file01.write(i + "\n")
        except BaseException as be:
            print(f"写文件异常，异常原因：{be}")
        else:
            print("写文件成功！")
        finally:
            file01.close()
    return True


if __name__ == "__main__":
    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\file06.txt"
    print(string.ascii_lowercase)
    print(create_file(file_path))

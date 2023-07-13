#!/usr/bin/env python
# coding:utf-8

"""
zip
    可以将不同的序列(列表、元组都叫序列)打包在一起
    返回一个个的元组(tuple)，每一个元组中都是被打包序列中的各自的一个元素

    zip函数可以将多个序列同时打包在一起，不只是2个，可以是3个
"""

import string


def zip_test():
    a = [1, 2, 3]
    b = (4, 5, 6)
    for num in range(0, len(a)):
        print(a[num] + b[num])

    for i, j in zip(a, b):
        print(i + j)

    for num in zip(a, b):
        print(num)
        print(type(num))


def create_file(file_path_in):
    """
    将所有小写字母写入文件，每行两个

    string.ascii_lowercase是所有小写字母的字符串
    从头开始，按步长2获取子列表
    从第二位开始，按步长2获取子列表
    使用zip将两个列表打包到一起
    使用for变量打包后的列表，每次遍历的结果是一个元组，包含两个元素，分别赋给两个遍历
    :param file_path_in:
    :return:
    """
    with open(file_path_in, "w+", encoding="utf-8") as file01:
        try:
            # string.ascii_lowercase是所有小写字母的字符串
            # 从头开始，按步长2获取子列表
            # 从第二位开始，按步长2获取子列表
            # 使用zip将两个列表打包到一起
            # 使用for变量打包后的列表，每次遍历的结果是一个元组，包含两个元素，分别赋给两个遍历
            for i, j in zip(string.ascii_lowercase[::2], string.ascii_lowercase[1::2]):
                file01.write(i + j + "\n")
        except BaseException as be:
            print(f"写文件异常，异常原因：{be}")
        else:
            print("写文件成功！")
        finally:
            file01.close()
    return True


if __name__ == "__main__":
    zip_test()

    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\file07.txt"
    print(create_file(file_path))
    print(string.ascii_lowercase[::2], string.ascii_lowercase[1::2])

#!/usr/bin/env python
# coding=utf-8
import math
import string
import file


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
            # 从头开始，按步长3获取子列表
            # 从第二位开始，按步长3获取子列表
            # 从第三位开始，按步长3获取子列表
            # 使用zip将三个列表打包到一起
            # 使用for变量打包后的列表，每次遍历的结果是一个元组，包含两个元素，分别赋给两个遍历
            # 26个字母分到3个字符串，第三个字符串少一个字符。zip打包后是空，需要特殊处理
            for x, y, z in zip(string.ascii_lowercase[::3],
                               string.ascii_lowercase[1::3],
                               string.ascii_lowercase[2::3].ljust(math.ceil(len(string.ascii_lowercase) / 3), " ")):
                file01.write(x + y + (z if z is not None else " ") + "\n")
                # print(x)
                # print(y)
                # print(z)
        except BaseException as be:
            print(f"写文件异常，异常原因：{be}")
        else:
            print("写文件成功！")
        finally:
            file01.close()
    return True


if __name__ == "__main__":
    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\file08.txt"
    print(create_file(file_path))
    print(string.ascii_lowercase[::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3])

#!/usr/bin/env python
# coding:utf-8

"""
zip
    可以将不同的序列(列表、元组都叫序列)打包在一起
    返回一个个的元组(tuple)，每一个元组中都是被打包序列中的各自的一个元素

    zip函数可以将多个序列同时打包在一起，不只是2个，可以是3个
"""
import datetime
import os
import string
import zipfile


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


def get_zip_file(path: str):
    """
    压缩path路径下的文件，存储在path路径中
    ~$格式的文件是临时文件，需要忽略
    .zip格式的文件是以及压缩好的文件，需要忽略
    string.startswith: 判断字符串前缀
    string.endswith: 判断字符串后缀
    zipfile.ZipFile: 打开压缩文件
    os.walk(path): 扫描path路径下所有路径及文件
    os.path.relpath(filepath, tarpath): 获取相对路径(filepath相对于tarpath的路径)
    zip_file.write(filepath): 压缩文件中显示绝对路径
    zip_file.write(filepath, writepath): 压缩文件中显示相对路径
    :param path:
    :return:
    """
    # 变更路径
    os.chdir(path)
    print("压缩文件存放路径：", os.getcwd())
    # 获取压缩文件名称: 文件夹名称-datetime格式化时间.zip
    zip_name = os.path.basename(path) + "-" + datetime.datetime.today().strftime("%Y%m%d%H%M%S") + ".zip"
    print("压缩文件名：", zip_name)
    # 打开压缩文件
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for root_file, sub_file, filelist in os.walk(path):
            for file in filelist:
                if not file.startswith("~$") and not file.endswith(".zip"):
                    filepath = os.path.join(root_file, file)
                    tarpath = os.path.dirname(path)
                    print(filepath)
                    # 压缩文件中显示绝对路径
                    # zip_file.write(filepath)
                    # 获取相对路径
                    writepath = os.path.relpath(filepath, tarpath)
                    # 压缩文件中显示相对路径
                    zip_file.write(filepath, writepath)
        zip_file.close()
    return


if __name__ == "__main__":
    zip_test()

    file_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\file\\file07.txt"
    print(create_file(file_path))
    print(string.ascii_lowercase[::2], string.ascii_lowercase[1::2])

    file_path = r"D:\02helloWorld\03Python\a01pythonLearn\file"
    get_zip_file(file_path)
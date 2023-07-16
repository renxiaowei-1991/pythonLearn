#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import string

import file

BASE_PATH = "D:\\02helloWorld\\03Python\\a01pythonLearn\\"


def create_func():
    file_path = "file\\"
    print(os.getcwd())
    os.chdir(BASE_PATH)
    print(os.getcwd())
    create_path = BASE_PATH + file_path + "p054"
    if not os.path.exists(create_path):
        os.mkdir(create_path)
    else:
        print(f"目录 {create_path} 已存在。")
    for i in string.ascii_lowercase:
        with open(create_path + "\\" + i + ".txt", "w+", encoding="utf-8") as file01:
            try:
                file01.write(i)
            except BaseException as be:
                print(f"写文件 {i}.txt 异常，异常原因：{be}")
            else:
                print(f"写文件 {i}.txt 成功")
            finally:
                file01.close()
    print("写文件结束")



if __name__ == "__main__":
    create_func()
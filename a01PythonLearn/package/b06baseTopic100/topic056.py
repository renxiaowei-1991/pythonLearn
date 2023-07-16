#!/usr/bin/env python
# -*- utf-8 -*-
import glob

import file
import os

BASE_PATH = "D:\\02helloWorld\\03Python\\a01pythonLearn\\"
file_path = "file\\p054"

print("扫描目录所有文件，方法二")
print(glob.glob(BASE_PATH + file_path + "\\*.txt"))
rs_list: list = []
for f in glob.glob(BASE_PATH + file_path + "\\*.txt"):
    rs_str: str = ""
    file01 = open(f, "r+", encoding="utf-8")
    for s in file01.read().strip():
        if s in "python":
            rs_str += s
    rs_list.append(rs_str) if rs_str != "" else None
print(rs_list)


#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import file
import pymysql
import xlrd3
import xlwt
import xlutils3
from package.b04ExeModule import c04FileIOType


def opera_excel():
    """
    读取excel文件内容，返回读取结果：二维数组
    :return:
    """
    base_path = "D:\\03gitHub\\pythonLearn\\a01PythonLearn\\excel\\"
    file_name = "xlrdLearn.xls"
    # 添加formatting_info=True后打开的文件可以获取单元格的详细信息
    # 例如：cell_type，如果不加参数，获取的到的值都是0，1，表示有没有数据。添加参数后获取到的值为真实的类型
    # 0. empty（空的）,1 string（text）,2 number,3 date,4 boolean,5 error,6 blank（空白表格）
    data = xlrd3.open_workbook(base_path + file_name, formatting_info=True)
    table01 = data.sheets()[1]
    print(type(table01.nrows))
    print(type(table01.ncols))
    table01_list_type = []
    table01_list_value = []
    table01_row_type = []
    table01_row_value = []
    for rown in range(table01.nrows):
        table01_row_type = []
        table01_row_value = []
        for coln in range(table01.ncols):
            table01_row_type.append(table01.cell_type(rown, coln))
            table01_row_value.append(table01.cell_value(rown, coln))
        table01_list_type.append(table01_row_type)
        table01_list_value.append(table01_row_value)

    print(table01_list_type)
    print(table01_list_value)
    return table01_list_value


def opera_excel_xf():

    base_path = "D:\\03gitHub\\pythonLearn\\a01PythonLearn\\excel\\"
    file_name = "xlrdLearn.xls"
    data = xlrd3.open_workbook(base_path + file_name, formatting_info=True)
    table01 = data.xf_list[1]
    print(type(table01.nrows))
    print(type(table01.ncols))
    table01_list_type = []
    table01_list_value = []
    table01_row_type = []
    table01_row_value = []
    for rown in range(table01.nrows):
        table01_row_type = []
        table01_row_value = []
        for coln in range(table01.ncols):
            table01_row_type.append(table01.cell_type(rown, coln))
            table01_row_value.append(table01.cell_value(rown, coln))
        table01_list_type.append(table01_row_type)
        table01_list_value.append(table01_row_value)

    print(table01_list_type)
    print(table01_list_value)
    return


if __name__ == "__main__":
    excel_file = opera_excel()
    base_path = "D:\\03gitHub\\pythonLearn\\a01PythonLearn\\file\\"
    file_name = "file06.txt"
    c04FileIOType.write_file_func(base_path + file_name, excel_file)



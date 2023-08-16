#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import csv


def csv_writer_learn():
    if not os.path.exists('./file'):
        os.mkdir('./file')

    # 用with打开csv文件，使用完后会自动关闭
    with open('./file/csvTest.csv', 'w', encoding='utf-8', newline='') as f:
        # 创建csv写文件对象
        writer = csv.writer(f)
        # wirterow() : 写一行(参数是列表，如果传字符串，会把字符串当成列表处理)
        lin = ['111', '222']
        writer.writerow(lin)
        # wirterows() : 写多行(参数是二维列表：如果是传一维列表，会把字符串当成列表处理)
        lins = [['111', '222'], ['222']]
        writer.writerows(lins)

        # 传csv写文件对象：按照字典格式写文件
        dictWriter = csv.DictWriter(f, fieldnames=['标题', '价格', '评率', '店铺'])
        # 写入文件头(标题行)
        dictWriter.writeheader()
        # 写入一行数据(参数是字典)
        dic = {
            '标题': '测试',
            '价格': '100',
            '评率': '5w+',
            '店铺': '开心就好',
        }
        dictWriter.writerow(dic)
        # 写入多行数据(参数是字典列表)
        dic1 = {
            '标题': '测试1',
            '价格': '100',
            '评率': '5w+',
            '店铺': '开心就好',
        }
        dic2 = {
            '标题': '测试2',
            '价格': '100',
            '评率': '5w+',
            '店铺': '开心就好',
        }
        dics = [dic1, dic2]
        dictWriter.writerows(dics)
        # 通过DictWriter的对象创建了一个writer对象
        # print(type(dictWriter.writer))
        dictWriter.writer.writerow(lin)


def csv_reader_learn():
    # 打开csv文件用于读取
    with open('./file/csvTest.csv', 'r', encoding='utf-8') as f:
        # 读取csv文件返回文件对象，可以转换为list，是一个迭代器
        reader = csv.reader(f)
        # 返回的对象只能读一次
        # print(reader.__next__())
        print(list(reader))
        for row in reader:
            print(row)


if __name__ == '__main__':
    # csv_writer_learn()
    csv_reader_learn()
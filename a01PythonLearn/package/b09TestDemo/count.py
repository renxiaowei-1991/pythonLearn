#!/usr/bin/env python
# -*- coding:utf-8 -*-

import file

def count(file_path_in, log_path_in):
    with open(file_path_in, "r+", encoding="utf-8") as file01,open(log_path_in, "w+", encoding="utf-8") as file02:
        b_num = 0
        k_num = 0
        m_num = 0
        g_num = 0
        b_num_count = 0
        k_num_count = 0
        m_num_count = 0
        g_num_count = 0
        try:
            for i in file01.readlines():
                if i.split(" ")[0] != "Found":
                    file02.write(" ".join(i.split()[4:6]) + "\n")
                    if i.split()[5] == "B":
                        b_num += float(i.split()[4])
                        b_num_count += 1
                    elif i.split()[5] == "K":
                        k_num += float(i.split()[4])
                        k_num_count += 1
                    elif i.split()[5] == "M":
                        m_num += float(i.split()[4])
                        m_num_count += 1
                    elif i.split()[5] == "G":
                        g_num += float(i.split()[4])
                        g_num_count += 1
                    else:
                        print("数据过大")
        except BaseException as be:
            print("处理异常，异常信息：", be)
        else:
            print("处理成功")
        finally:
            file01.close()
            file02.close()

        print("B大小文件数：", b_num_count, "B大小数据：", b_num)
        print("B大小文件数：", k_num_count, "K大小数据：", k_num)
        print("B大小文件数：", m_num_count, "M大小数据：", m_num)
        print("B大小文件数：", g_num_count, "G大小数据：", g_num)


if __name__ == "__main__":
    file_path = "/home/renxiaowei7/personal/renxiaowei7/temp/data.txt"
    log_path = "/home/renxiaowei7/personal/renxiaowei7/temp/log.txt"
    count(file_path, log_path)

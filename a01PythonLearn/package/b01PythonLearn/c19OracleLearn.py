#!/usr/bi/env python
# -*- coding:utf-8 -*-

import sys
import os
import cx_Oracle

"""
Oracle
  Oracle API
    cx_oracle

    https://blog.csdn.net/viviliving/article/details/109313731

"""


def OracleConn():
    # 用户名/密码@域名:端口/库名
    conn = cx_Oracle.connect('OracleLearn/OracleLearn@localhost:1521/orcl')
    curs = conn.cursor()
    sql = "select * from PARTITION_TEST01"
    res = curs.execute(sql)
    row = res.fetchone()
    print(row)

    conn.close()


if __name__ == "__main__":
    OracleConn()
    
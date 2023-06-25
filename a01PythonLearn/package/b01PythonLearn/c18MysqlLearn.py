#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import pymysql

"""
数据库
    Python标志数据库接口为 Python DB-API， Python DB-API 为开发人员提供了数据库应用编程接口。
    支持以下数据库：
    Mysql
    PostgreSQL
    Microsoft SQL Server 2000
    Oracle
    DB2
    Sybase
    Netezza
    Teradata
    ...

    不同的数据库需要下载不同的DB API模块
    DB-API是一个规范，定义了一系列必须的对象和数据库存取方式，以便为各种各样的底层数据库系统和多种多样的数据库接口程序提供一致的访问接口
    Python 的DB-API，为大多数的数据库实现了接口，使用它连接各种数据库后，就可以用相同的方式操作各数据库。

Python DB-API 使用流程
    引入API模块
    获取与数据库的链接
    执行SQL语句和存储过程
    关闭数据库链接

MySQL DB-API
    MySQLdb
        Python2.x,MySQLdb 是用于Python链接Mysql数据库的接口，它实现了Python数据库API规范V2.0，基于MySQL C API 建立的。
    PyMySQL
        Python3.x,PyMySQL是在Python3.x版本中用于连接MySQL服务器的一个库。


MySQLdb安装
    https://www.jb51.net/article/215631.htm
PyMySQL安装
    https://blog.csdn.net/weixin_39719749/article/details/109753056?utm_term=pymysql%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-0-109753056-null-null&spm=3001.4430

注意：
    增删改 操作，需要二次确认才可生效。
    conn.commit()

事务：
    对于支持事务的数据库，在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。
    commit()方法游标的所有更新操作，rollback()方法回滚当前游标的所有操作。
    每一个方法都开始了一个新的事务
"""

"""
MySQL数据库链接
"""


def connTest():
    # 打开数据库链接
    conn = pymysql.connect(
        host="localhost",  # 域名
        port=3306,  # 端口 可以没有
        user="pythonlearn01",  # 用户名
        password="pythonlearn01",  # 密码
        database="pythonlearn",  # 库名
        charset="utf8"  # 编码格式 可以没有，没有就使用默认值
    )

    # 使用cursor()方法获取操作游标
    # 生成一个游标对象(相当于cmd打开mysql中的 mysql>)
    cursor = conn.cursor()

    # SQL语句
    sql = "select * from pythonlearntest01"

    # 使用execute方法执行SQL语句
    # 执行sql后，要获取结果，需要从cursor获取
    # 返回的结果是元组的形式
    cursor.execute(sql)

    """
    fetchone()
        获取一条数据
        返回单个元组(类)，也就是一条记录(row)，如果没有结果，则返回None
    """
    dataone = cursor.fetchone()
    """
    fetchall()
        获取多条数据
        返回多个元组(类)，也就是多条记录(row)，如果没有结果，则返回None
    """
    dataall = cursor.fetchall()
    count = cursor.rowcount
    number = cursor.rownumber

    # 输出数据
    print(tuple(dataone))
    print(tuple(dataall))
    # for data in dataall:
    #    print("Database version : %s" % data)
    print("SQL查询结果条数:", count)
    print("SQL查询结果条数:", number)

    # 参数传递
    cursor.execute("select * from %s" % "employee01")
    print(list(cursor.fetchall()))

    # 关闭数据库链接
    conn.close()


def connDB(hostPar, portPar, userPar, passwordPar, databasePar):
    # 打开数据库链接
    conn = pymysql.connect(
        host=hostPar,
        port=portPar,
        user=userPar,
        password=passwordPar,
        database=databasePar,
        charset="utf8"
    )

    # 返回数据库连接
    return conn


def execSQL(hostPar, portPar, userPar, passwordPar, databasePar, sql):
    # 打开数据库连接
    conn = connDB(hostPar, portPar, userPar, passwordPar, databasePar)
    # 获取游标
    # cursor=pymysql.cursors.DictCursor  让数据自动组织成字典
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行sql
    try:

        cursor.execute(sql)
        # res=cursor.fetchall()
        # print(res)
        # 增删改 二次确认
        conn.commit()
    except:
        # 事务 回退
        conn.rollback()
    # 关闭数据库
    conn.close()


def mysqlTest():
    # SQL定义
    createSQl = """
    create table if not exists employee01(
         id int unsigned auto_increment
        ,first_name  varchar(40)   comment '名'   not null
        ,last_name   varchar(40)   comment '姓'   not null
        ,age         int           comment '年龄' not null
        ,sex         varchar(2)    comment '性别' not null
        ,income      decimal(22,2) comment '收入' not null
        ,primary key (id)
    ) comment '雇员表'
    engine=InnoDB charset=utf8
    ;
    """

    insertSQL = """
    insert into employee01(first_name,last_name,age,sex,income)
    values("小伟","任",30,"男",100000000);
    """

    selectSQL = """
    select * from employee01;
    """

    # 执行SQL
    # execSQL("localhost", 3306, "pythonlearn01", "pythonlearn01", "pythonlearn", createSQl)
    # execSQL("localhost", 3306, "pythonlearn01", "pythonlearn01", "pythonlearn", insertSQL)
    execSQL("localhost", 3306, "pythonlearn01", "pythonlearn01", "pythonlearn", selectSQL)


"""
数据库查询练习
"""


def test01():
    # 创建数据库链接
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="pythonlearn01",
        password="pythonlearn01",
        database="pythonlearn"
    )

    # 创建游标
    cursor = conn.cursor()

    # 执行sql
    database = "pythonlearn"
    tableName = "employee01"

    # 字段查询
    cursor.execute("""
    select column_name from information_schema.columns 
    where table_schema='%s'
    and table_name='%s'
    order by ordinal_position
    """ % (database, tableName)
                   )
    # 获取执行结果
    resHead = cursor.fetchall()
    for row in resHead:
        for col in row:
            print(col, end=" ")
    print()

    # 数据查询
    cursor.execute("select * from %s" % tableName)
    # 获取执行结果
    resBody = cursor.fetchall()
    for row in resBody:
        for col in row:
            print(col, end=" ")
        print()

    # 关闭数据库链接
    conn.close()


if __name__ == "__main__":
    # print("数据库链接练习")
    # connTest()
    # print("数据库链接学习")
    # mysqlTest()
    print("练习")
    test01()

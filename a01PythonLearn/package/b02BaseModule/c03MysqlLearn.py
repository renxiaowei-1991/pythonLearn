#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
from package.b03ClassModule.c01LogDeal import LogDeal


class SqlExecute:
    """
    连接池实现
    不关闭游标对象cursor 和 数据库对象db，就可以接着用，连接（db）应该不需要反反复复创建销毁，应该是多个cursor共享一个db.
    """
    # 连接池：安装数据库类型存储数据库连接
    db_conn = {}
    # 游标池：存储mysql数据库连接的cursor游标
    mysql_cursor = []

    def __init__(self):
        """
        构造函数
        """
        pass

    def __del__(self):
        """
        析构函数
        :return:
        """
        print("注销")

    @staticmethod
    def get_db_conn():
        """
        获取数据库连接，如果连接池已存在，则使用连接池的connect。
        如果连接池不存在对应数据库类型的连接，则新打开一个connect，并且把connect对象放到连接池中。
        :return:
        """
        try:
            if SqlExecute.db_conn.get('mysql') is None:
                conn = pymysql.connect(
                    host="192.168.56.100",
                    port=3306,
                    user="root",
                    password="root",
                    database="hive",
                    charset="utf8"
                )
                SqlExecute.db_conn['mysql'] = conn
            else:
                conn = SqlExecute.db_conn.get('mysql')
        except BaseException as be:
            LogDeal().write_log("获取连接失败, {}".format(be))
        return conn

    @staticmethod
    def add_cursors():
        """
        获取游标cursor存入游标池
        :return:
        """
        try:
            SqlExecute.mysql_cursor.append(SqlExecute.get_db_conn().cursor())
        except BaseException as be:
            LogDeal().write_log("获取连接失败, {}".format(be))

    @staticmethod
    def execute_sql(sql):
        """
        从游标池获取游标，执行sql语句
        :param sql:
        :return:
        """
        result = []
        # 如果游标池有游标对象，则直接使用，否则新建游标，存入游标池
        if len(SqlExecute.mysql_cursor) > 0:
            LogDeal().write_log("获取连接前，mysql当前连接池剩余链接数：{}".format(len(SqlExecute.mysql_cursor)))
            # 从数据库连接池获取连接
            cursor1 = SqlExecute.mysql_cursor.pop()
            LogDeal().write_log("获取连接后，mysql当前连接池剩余链接数：{}".format(len(SqlExecute.mysql_cursor)))
        else:
            LogDeal().write_log("获取连接前，mysql当前连接池剩余链接数为0，需要新建连接。")
            # 将新获取的数据库连接放入连接池
            SqlExecute.add_cursors()
            LogDeal().write_log("连接已新建，当前连接数：{}".format(len(SqlExecute.mysql_cursor)))
            cursor1 = SqlExecute.mysql_cursor.pop()
            LogDeal().write_log("连接已新建，获取连接后连接数：{}".format(len(SqlExecute.mysql_cursor)))
        try:
            # 执行sql
            cursor1.execute(sql)
            # 将执行结果转换成list
            for col in cursor1.fetchall():
                result.append(list(col))
        except BaseException as be:
            print("sql执行失败，失败信息为： {}".format(be))
        else:
            print("sql执行成功！")
        finally:
            # 使用完查询链接之后，再放回连接池
            SqlExecute.mysql_cursor.append(cursor1)
            LogDeal().write_log("查询已完成，将数据库连接放入连接池，放入后连接数：{}".format(len(SqlExecute.mysql_cursor)))
        return result

    @staticmethod
    def execute_sql_file(filename):
        """
        从游标池获取游标，从指定文件获取sql语句，执行sql
        :param filename:
        :return:
        """
        result = ""
        sql = ""
        try:
            sql_file = open(filename, 'r+', encoding='utf-8')
            sql_list = [line for line in sql_file.readlines()]
            sql = "".join(sql_list)
            LogDeal().write_log("从sql文件获取的最终sql为：\n {}".format(sql))
        except BaseException as be:
            LogDeal().write_log("读取sql文件异常，异常原因：{}".format(be))
        result = SqlExecute.execute_sql(sql)
        return result

    @staticmethod
    def clear_db_conn():
        try:
            if SqlExecute.db_conn['mysql'] is not None:
                SqlExecute.db_conn['mysql'].close()
        except BaseException as be:
            LogDeal().write_log("关闭数据库连接失败，报错信息是：{} \n".format(be))
        else:
            LogDeal().write_log("关闭数据库连接成功！\n")
        finally:
            print("关闭数据库连接结束！")





tableName = "TBLS"
sql01 = "select * from {tableName}".format(tableName=tableName)
result = SqlExecute.execute_sql(sql01)
print(result)
# base_path = "D:\\02helloWorld\\03Python\\a01pythonLearn\\sql\\"
# file_name = "createTable01.sql"
# result = SqlExecute.execute_sql_file(base_path + file_name)
# print(result)
# print(type(SqlExecute.conn))
SqlExecute.clear_db_conn()


#!/use/bin/env python
# -*- coding:utf-8 -*-

import time
import calendar
import datetime

#获取月初日期
def get_month_start(in_date):
    in_year, in_month, in_day = str(in_date).split('-')
    out_year = in_year
    out_month = in_month
    out_day = "01"
    list_date = [out_year, out_month, out_day]
    # split_str = "-"
    out_date = "-".join(list_date)
    return out_date

"""
    python实现add_months
    有bug
        add_months('2022-03-31',-1) 是 '2022-02-31'，而不是'2022-02-28'
"""
def get_add_months(in_date, num):
    in_year, in_month, in_day = str(in_date).split('-')
    # print(in_year,in_month,in_day)
    if (int(in_month) + num) % 12 == 0:
        out_year = str(int(in_year) + (int(in_month) + num) // 12 - 1)
        out_month = str("12")
    else:
        out_year = str(int(in_year) + (int(in_month) + num) // 12)
        out_month = str((int(in_month) + num) % 12).zfill(2)  # 月份补齐两位

    out_day = in_day
    # print(out_year,out_month,out_day)
    list_date = [out_year, out_month, out_day]
    # split_str = "-"
    out_date = "-".join(list_date)
    return out_date

#date_add实现
def date_add(date1,num):
    #接收10位日期参数，并转换为时间元组
    date2 = time.strptime(date1, "%Y-%m-%d")
    #将日期转换为时间戳
    date3 = time.mktime(date2)
    #将日期计算后转换为时间元组
    date4 = time.localtime(date3+num*24*60*60)
    #件日期转换为格式化时间
    #date6 = time.strftime("%Y-%m-%d %H:%M:%S", date4)
    date6 = time.strftime("%Y-%m-%d", date4)
    #返回格式化时间
    return date6

"""
    python实现add_months
    bug已修复
        add_months('2022-03-31',-1) 是 '2022-02-28'，而不是'2022-02-31'
"""
def add_months(in_date,num):
    #将10位格式化日期转换成时间元组
    par_date = time.strptime(in_date,"%Y-%m-%d")
    in_year, in_month, in_day = par_date.tm_year, par_date.tm_mon, par_date.tm_mday
    #print(in_year,in_month,in_day)
    #年月处理
    if (int(in_month) + num) % 12 == 0:
        out_year = str(in_year+ (in_month + num) // 12 - 1)
        out_month = str("12")
    else:
        out_year = str(in_year + (in_month + num) // 12)
        out_month = str((in_month + num) % 12).zfill(2)  # 月份补齐两位

    """
        #日处理
        获取上月末日期
        e.g. add_months('2022-03-31',-1) 应该是 '2022-02-28'，而不是'2022-02-31'
    """
    last_mon_day = date_add(get_month_start(in_date),-1)
    last_mon_day_mday = time.strptime(last_mon_day, "%Y-%m-%d").tm_mday
    if last_mon_day_mday < in_day :
        out_day = str(last_mon_day_mday).zfill(2)
    else:
        out_day = str(in_day).zfill(2)

    #print(out_year,out_month,out_day)
    list_date = [out_year, out_month, out_day]
    # split_str = "-"
    out_date = "-".join(list_date)
    return out_date



print("日期计算")
date1 = time.strftime("%Y-%m-%d",time.localtime())
print(date_add(date1,-1))
print(get_month_start('2022-04-12'))

print("add_months实现")
print("有bug",get_add_months("2022-03-31",-1))
print("无bug",add_months("2022-03-31",-1))

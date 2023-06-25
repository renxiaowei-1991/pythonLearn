#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import calendar
import datetime

"""
    日期&时间
        time 和 calendar 模块用于格式化日期和时间
        时间间隔是以秒为单位的浮点小数
        每个时间戳都以从1970年1月1日午夜(历元)经过了多长时间来表示
        time模块有很多函数可以转换常见日期格式
        时间戳格式适用于做日期计算，1970之前的日期不行，太靠后的日期也不行，unix、windows只支持到2038年

    时间元组(struct_time)
        python函数用一个元组装起来的9组数字处理时间
        序号  字典        值
        0    4位数年      2008
        1    月          1-12
        2    日          1-31
        3    小时        0-23
        4    分钟        0-59
        5    秒          0-61(60,61是闰秒)
        6    一周的第几日  0-6(0是周一)
        7    一年的第几日  1-366(儒略历)
        8    夏令时       -1,0,1,-1是决定是否为夏令时的旗帜

    struct_time元组
        序号  属性      值
        0    tm_year  2008
        1    tm_mon   1-12
        2    tm_mday  1-31
        3    tm_hour  0-23
        4    tm_min   0-59
        5    tm_sec   0-61
        6    tm_wday  0-6
        7    tm_yday  1-366
        8    tm_isdst -1,1,1

    模块
        datetime(日期时间)模块主要用来表示日期的，就是常说的年月日时分秒
        calendar(日历)模块主要用来表示年月日，是星期几之类的
            日历的展示
        time(时间)模块主要侧重点在时分秒。
            时间的获取，及时间格式的转换
        三者关系互补

        time模块是一个基础模块，可以满足对时间类型数据的基本处理
        datetime模块可以看做是对time模块的一个高级封装

        time模块解决了时间的获取和表示
        datetime进一步解决了快速获取并操作时间中的年月日时分秒信息的能力

        https://www.cnblogs.com/Hardworking666/p/15866132.html
        https://baijiahao.baidu.com/s?id=1666748705793386009&wfr=spider&for=pc


    time模块(时间)
        time.time()                  获取当前时间戳
        time.localtime()             时间元组
        time.localtime(时间戳)        时间戳-->时间元组
            如果没有参数，默认取当前时间
        time.asctime()              标准时间
        time.asctime(时间元组)        时间元组-->标准时间(最简单的获取可读时间模式的函数)  
            如果没有参数，默认取当前时间
        time.strftime(format[, t(时间元组)])   格式化日期
            如果没有时间参数，默认取当前时间
        time.strptime(t,"%Y-%m-%d %H:%M:%S")
            将格式化时间转换成时间元组
        time.mktime()
            将时间元组转换成时间戳

        time.mktime(time.strptime(t,"%Y-%m-%d %H:%M:%S"))
            将格式化日期转换成时间戳

        time.sleep(secs)
            调用线程的运行，secs指秒数

    calendar模块(日历)
        calendar模块有广泛的方法用来处理年历和月历。
        此模块的函数都是和日历相关的

        calendar.calendar(year,w=2,I=1,c=6)
            返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。每日宽度间隔为w字符。
            每行长度为21*W+18+2*C。
            l是没星期行数
        calendar.month(年,月)  打印**年**月的日历
            返回的是带换行的字符串
        calendar.firstweekday()
        calendar.setfirstweekday()
            设置每周第一天的开始天。
            默认星期一是每周第一天，星期天是最后一天。setfirstweekday可以设置开始的星期
        calendar.isleap(year)
            判断year是否是闰年
        calendar.weekday(year,month,day)
            返回给定日期的日期码。0(星期一)-6(星期日)

    datetime模块(日期时间)
        常用类
        date      日期类
            year
            month
            day
        time      时间类
            hour
            minute
            second
            microsecond
        datetime  日期时间类型
        datedelta 时间间隔，即两个时间点之间的时间长度
        tzinfo    时区类

        2个常量
            datetime.MINYEAR  date和datetime对象允许的最小年份
            datetime.MAXYEAR  date和datetime对象允许的最大年份

        多个属性
            datetime.date      日期对象，属性(year,month,day)
                方法  today()  通过today方法可以获取当前日期的date对象
            datetime.time      时间对象，属性(hour,minute,second,microsecond,tzinfo)
            datetime.datetime  日期时间对象，属性(date和time属性)
                方法  today()  通过today方法可以获取当前日期的datetime对象
                      now()    通过now方法可以获取当前日期的datetime对象
            datetime.datedelta Difference between two datetime values(原文)
            datetime.tzinfo    时区信息对象的抽象基类，datetime和time类使用它定制化时间调节


    时间日期格式化符号
        %y  两位数的年份表示(00-99)
        %Y  四位数的年份表示(0000-9999)
        %m  月份(01-12)
        %d  月内中的一天(0-31)
        %H  24小时制小时数(0-23)
        %I  12小时制小时数(01-12)
        %M  分钟数(00-59)
        %S  秒(00-59)
        %a  本地简化星期名称
        %A  本地完整星期名称
        %b  本地简化的月份名称
        %B  本地完整的月份名称
        %c  本地相应的日期表示和时间表示
        %j  年内的一天(001-366)
        %p  本地A.M.或者P.M.的等价符
        %U  一年中的星期数(00-53)星期天为星期的开始
        %w  星期(0-6)，星期一为星期的开始
        %x  本地相应的日期表示
        %X  本地相应的时间表示
        %Z  当前时区的名称
        %%  %号本身



"""
print("time模块练习")
print("1、时间戳获取")
time1 = time.time()
print("当前时间戳：", time1)

print("2、时间元组练习")
time2 = time.localtime(time.time())
print("当前时间时间元组：", time2)
print("当前时间时间元组：", time.localtime())
print("当前时间时间元组：", time.localtime(time.time()))
# print(time2['tm_year'])
print(time2[0])

print('"3、标准时间格式练习')
time3 = time.asctime(time2)
print("标准时间格式：", time3)
print("当前标准格式时间：", time.asctime())
print("当前标准格式时间：", time.asctime(time.localtime()))
print("当前标准格式时间：", time.asctime(time.localtime(time.time())))

print("4、格式化日期练习：")
time4 = time.localtime()
print("格式化日期：", time.strftime("%Y-%m-%d %H:%M:%S"))
print("格式化日期：", time.strftime("%Y-%m-%d %H:%M:%S", time4))
print("格式化日期：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("格式化日期：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
print("格式化日期：", time.strftime("%a-%b-%d %H:%M:%S %Y"))

print("5、格式化日期转换时间戳：")
time5 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time5)

print("6、格式化日期转换时间元组：")
print(time.strptime(time5, "%Y-%m-%d %H:%M:%S"))

print("7、格式化日期转换时间戳：")
print(time.mktime(time.strptime(time5, "%Y-%m-%d %H:%M:%S")))

print("日期格式化符号")
print(time.strftime("%x %X"))

print("calendar模块练习")
print("打印year年的年日历")
print(calendar.calendar(2022))
print(calendar.calendar(2022, w=2, l=1, c=6))
print(type(calendar.calendar(2022)))
print("打印year,month的月日历")
print(calendar.month(2022, 4))
print(type(calendar.month(2022, 4)))
print(calendar.month(2022, 4)[0:20])
print("返回当前每周开始日，0表示星期一")
print(calendar.firstweekday())
print(calendar.month(2022, 4))
print("设置星期四为每周起始日")
calendar.setfirstweekday(3)
print(calendar.firstweekday())
print(calendar.month(2022, 4))
print("返回参数日期是星期几")
print(calendar.weekday(2022, 4, 12))
print(type(calendar.weekday(2022, 4, 12)))
print("返回参数日期是星期几：", calendar.weekday(2022, 4, 12))
print(['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'][calendar.weekday(2022, 4, 11)])
weekd = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
print(weekd[calendar.weekday(2022, 4, 11)])

print("datetime模块练习")
print(datetime.date.today().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)
print(datetime.datetime.today())
print(datetime.datetime.now())

print("时间计算")
date1 = time.time()
date2 = time.strptime("2022-04-12", "%Y-%m-%d")
date3 = time.mktime(date2)
date4 = time.localtime(date3 + 2 * 24 * 60 * 60)
date5 = time.asctime(date4)
date6 = time.strftime("%Y-%m-%d %H:%M:%S", date4)
print(date1)
print(date2)
print(date3)
print(date4)
print(date5)
print(date6)



print("时间练习:")
# 获取当前时间时间戳
print(time.time())
# 获取当前时间时间元组
print(time.localtime())
# 获取当前时间时间元组-年
print(time.localtime().tm_year)
# 时间戳->(计算)->时间元组
print(time.localtime(time.time() + 24 * 60 * 60))
# 获取当前时间标准时间
print(time.asctime())
# 时间戳->(计算)->时间元组->标准时间
print(time.asctime(time.localtime(time.time() + 24 * 60 * 60)))

# 当前时间(时间元组)->格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 时间元组->格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 时间戳->(计算)->时间元组->格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 24 * 60 * 60)))

# 格式化时间->时间元组
print(time.strptime("2023-06-23 17:24:21", "%Y-%m-%d %H:%M:%S"))
# 时间元组->时间戳
print(time.mktime(time.localtime()))
# 格式化时间->时间元组->时间戳
print(time.mktime(time.strptime("2023-06-23 17:28:23", "%Y-%m-%d %H:%M:%S")))


print("sql函数功能实现")
def date_add(tx_date, tx_num):
    """
    python实现sql的date_add函数功能
    :param tx_date:10位日期
    :param tx_num:日期加减的整数
    :return:返回计算后的10为日期
    """
    # 输入的格式化日期转时间戳(格式化时间->时间元组->时间戳)
    in_date = time.mktime(time.strptime(tx_date, "%Y-%m-%d"))
    # 对时间戳进行计算后转格式化日期(# 时间戳->(计算)->时间元组->格式化时间)
    out_ate = time.strftime("%Y-%m-%d", time.localtime(in_date + tx_num * 24 * 60 * 60))
    return out_ate


def date_sub(tx_date, tx_num):
    """
    python实现sql的date_sub函数功能
    :param tx_date:10位日期
    :param tx_num:日期加减的整数
    :return:返回计算后的10为日期
    """
    # 输入的格式化日期转时间戳(格式化时间->时间元组->时间戳)
    in_date = time.mktime(time.strptime(tx_date, "%Y-%m-%d"))
    # 对时间戳进行计算后转格式化日期(# 时间戳->(计算)->时间元组->格式化时间)
    out_ate = time.strftime("%Y-%m-%d", time.localtime(in_date - tx_num * 24 * 60 * 60))
    return out_ate


def get_month_start(tx_date):
    """
    python实现sql的获取月初日期函数功能
    :param tx_date: 10位日期
    :return: 返回月初日期
    """
    # 拆分输入日期
    in_year, in_month, in_day = str(tx_date).split('-')
    # 日期中的日改为01
    out_year, out_month, out_day = in_year, in_month, "01"
    # 使用-拼接输出结果
    return '-'.join([out_year, out_month, out_day])


def add_months_init(tx_date, tx_num):
    """
    python实现sql的add_months函数功能
    这里是预计算，后续还需对日期中"日"的部分进行修正
    例如：add_months_init("2020-06-30", -4)，结果是2020-02-30，是错误的，所以需要对日进行修正，修正过程在真正的add_months中进行
    :param tx_date: 10位日期
    :param tx_num: 月份加减的整数
    :return: 返回计算后的10为日期
    """
    # 输入的格式化日期拆分成年,月,日
    in_year_s, in_month_s, in_day_s = str(tx_date).split('-')
    # 输入时间的年,月,日转数值类型，方便计算
    in_year_i, in_month_i, in_day_i = int(in_year_s), int(in_month_s), int(in_day_s)

    # 计算年
    # 年的变化是输入日期月+变化月数后，减1，对12整除
    out_year = str(in_year_i + (in_month_i + tx_num - 1) // 12)

    # 计算月
    # 对月份计算后进行判断
    if (in_month_i + tx_num) % 12 == 0:
        in_month_i = 12
    else:
        in_month_i = (in_month_i + tx_num) % 12
    # zfill(0)将字符串进行右对其，使用0补齐到2位宽。等价与rjust(2,"0")
    out_month = str(in_month_i).zfill(2)

    # 计算日
    out_day = str(in_day_i)

    # 将计算好的年/月/日,使用-拼接到一起
    return "-".join([out_year, out_month, out_day])


def add_months(tx_date, tx_num):
    """
    对add_months_init的初步计算结果进行修正，add_months_init的结果中"日"的部分是有问题的。
    例如：add_months_init("2020-06-30", -4)，结果是2020-02-30，是错误的，所以需要对日进行修正，修正过程在这里进行
    :param tx_date: 10位日期
    :param tx_num: 月份加减的整数
    :return: 返回计算后的10为日期
    """
    # 利用add_months_init对日期进行初步计算(日的值有问题)
    tx_date_init = add_months_init(tx_date, tx_num)
    """
    1) 对初步计算的结果月份+1
    2) 对月份+1后的日期取月初
    3) 对下月月初的日期-1
    4) 如果经过这三步计算的结果与add_months_init的初步计算结果一致，说明初步计算结果没问题，否则就是有问题。总之，直接使用重新计算后的结果即可
    """
    out_date = date_sub(get_month_start(add_months_init(tx_date_init, 1)), 1)
    return out_date


print(date_add("2023-06-21", 10))
print(date_sub("2023-06-21", 10))
print(add_months("2020-06-30", -4))



# 获取指定年份的日历
print(calendar.calendar(2023))
print(calendar.calendar(2023, w=2, c=1))
print(calendar.calendar(2023, w=2, c=12))
print(calendar.calendar(2023, w=2, c=12, l=1, m=3))
print(calendar.month(2023, 6))
print(calendar.weekday(2023, 6, 22))


# datetime模块
# 使用today()方法获取date对象
print(datetime.date.today())
# 获取当前日期date对象的year属性
print(datetime.date.today().year)
# 获取当前日期date对象的month属性
print(datetime.date.today().month)
# 获取当前日期date对象的day属性
print(datetime.date.today().day)

# 获取time对象
# print(datetime.time())

# 使用today()方法获取datetime对象
print(datetime.datetime.today().year)
print(datetime.datetime.today().month)
print(datetime.datetime.today().day)
print(datetime.datetime.today().hour)
print(datetime.datetime.today().minute)
print(datetime.datetime.today().second)
# 使用now()方法获取datetime对象
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().second)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

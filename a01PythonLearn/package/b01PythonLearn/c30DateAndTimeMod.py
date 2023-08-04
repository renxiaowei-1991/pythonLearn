import datetime
import time

"""
类型转换：
    转换的时候只有浮点和字符串可以转换为时间元组。时间元组可以转换为浮点和字符串。
    浮点(时间戳)->时间元组->字符串(格式化时间&标准时间)
    字符串(格式化时间&标准时间)->时间元组->浮点(时间戳)

注意：
    时间戳，(格式化时间&标准时间)，与时间格式的转换，都需要先转换成时间格式。
    datetime,time相当于中间桥梁

time模块 日期+时间
    time.time() : 时间戳(浮点类型)
    time.localtime() : 时间元组(元组)
    time.strftime("%Y-%m-%d", time.localtime()) : 格式化时间(字符串)("%Y-%m-%d %H:%M:%S")
    time.asctime() : 标准时间(字符串)("%a %b %d %H:%M:%S %Y")

    time.strptime("2023-07-15 14:04:00", "%Y-%m-%d %H:%M:%S") : 时间元组(格式化时间转换)
    time.mktime(time.localtime() : 时间元组(标准时间转换)
    time.gmtime(time.time()) : 时间元组(UTC时区(0时区))(时间戳转换)

datetime模块
    https://zhuanlan.zhihu.com/p/380756438

    对time模块的封装
    datetime.date class 日期
        datetime.date 转字符串(格式化时间&标准时间) + 转时间元组。配合time模块的方法，进行date处理

        初始化
            datetime.date(year=2023, month=7, day=15)
            datetime.date.today()
        datetime.date->字符串(格式化时间&标准时间)
            datetime.date.today().ctime()
            datetime.date.today().strftime("%a %b %d %H:%M:%S %Y")
            datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
        datetime.date->时间元组
            datetime.date.today().timetuple()

    datetime.time class 时间
        初始化
            datetime.time(13, 29, 30)
        datetime.time->字符串(格式化时间&标准时间)
            datetime.time(14, 8, 30).strftime("%H:%M:%S")

    datetime.datetime class 日期+时间
        datetime.datetime 转字符串(格式化时间&标准时间) + 转时间元组 + 浮点类型(时间戳)。配合time模块的方法，进行datetime处理
        格式化时间 转 datetime.datetime 。配合time模块的方法，进行datetime处理

        初始化
            datetime.datetime(2023, 7, 16, 16, 14, 30)
            datetime.datetime.today()
            datetime.datetime.now()
        date+time
            datetime.datetime.today().date()
            datetime.datetime.today().time()
        datetime.datetime()->字符串(格式化时间&标准时间)
            datetime.datetime.today().ctime()
            datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            datetime.datetime.today().strftime("%a %b %d %H:%M:%S %Y")
        datetime.datetime()->时间元组
            datetime.datetime.today().timetuple()
        格式化时间->时间元组
            datetime.datetime.strptime("2023-07-16 14:23:30", "%Y-%m-%d %H:%M:%S")
            datetime.datetime.today().strptime("2023-07-16 14:23:30", "%Y-%m-%d %H:%M:%S")
        datetime.datetime()->时间戳
            datetime.datetime.today().timestamp()
        时间戳->datetime.datetime()
            datetime.datetime.fromtimestamp(1689504035.058669)

    datetime.timedelta class 时间加减-时间间隔
        得到的是时间间隔对象。可以让datetime对象对时间进行加减运算
              
        对日期&时间 进行计算，用来指定对时间进行加减的间隔
        datetime格式的才能和timedelta进行计算.
        time.localtime()格式的不能和timedelta进行计算
        
        datetime - datetime 结果是 datetime.timedelta 类型

        datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
            间隔一天
        datetime.timedelta(days=1) 间隔一天
        datetime.timedelta(days=1, weeks=1) 间隔一天+一周
        datetime.timedelta(days=1, weeks=1, hours=1) 间隔一天+一周+1小时

    datetime.timezone class
        timezone 类是 tzinfo 的子类，它的每个实例都代表一个以与 UTC 的固定时差来定义的时区

    datetime.tzinfo class

"""
print("time模块: ")
print(time)
print("time模块: 时间戳->时间元组->格式化时间&标准时间")
print("时间戳: ", time.time(), ", 类型: ", type(time.time()))  # 时间戳
print("时间元组: ", time.localtime())  # 时间元组
print("时间元组(时间戳转换): ", time.localtime(time.time()), ", 类型: ", type(time.localtime()))  # 时间元组
print("时间元组(UTC时区(0时区))(时间戳转换)", time.gmtime(time.time()), ", 类型: ", type(time.gmtime(time.time())))
print("格式化时间(时间元组转换): ", time.strftime("%Y-%m-%d", time.localtime()), ", 类型: ",
      type(time.strftime("%Y-%m-%d", time.localtime())))
print("标准时间(时间元组转换): ", time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), ", 类型: ",
      type(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())))
print("标准时间(时间元组转换): ", time.asctime(time.localtime()), ", 类型: ", type(time.asctime()))
print("标准时间(默认值转换): ", time.asctime(), ", 类型: ", type(time.asctime()))
print("标准时间(默认值转换): ", time.ctime(), ", 类型: ", type(time.ctime()))

print("\ntime模块: 格式化时间&标准时间->时间元组->时间戳")
print("时间元组(格式化时间转换)", time.strptime("2023-07-15 14:04:00", "%Y-%m-%d %H:%M:%S"), ", 类型: ",
      type(time.strptime("2023-07-15 14:04:00", "%Y-%m-%d %H:%M:%S")))
print("时间元组(标准时间转换)(默认格式)", time.strptime(time.asctime()), ", 类型: ",
      type(time.strptime(time.asctime())))
print("时间元组(标准时间转换)(指定格式)", time.strptime(time.asctime(), "%a %b %d %H:%M:%S %Y"), ", 类型: ",
      type(time.strptime(time.asctime(), "%a %b %d %H:%M:%S %Y")))
print("时间戳(时间元组转换): ", time.mktime(time.localtime()), ", 类型: ", type(time.mktime(time.localtime())))

print("\ntime模块: 获取时间元组元素")
print("时间(年): ", time.localtime().tm_year, ", 类型: ", type(time.localtime().tm_year))
print("时间(月): ", time.localtime().tm_mon, ", 类型: ", type(time.localtime().tm_mon))
print("时间(日/月): ", time.localtime().tm_mday, ", 类型: ", type(time.localtime().tm_mday))
print("时间(日/周): ", time.localtime().tm_wday, ", 类型: ", type(time.localtime().tm_wday))
print("时间(日/年): ", time.localtime().tm_yday, ", 类型: ", type(time.localtime().tm_yday))
print("时间(时): ", time.localtime().tm_hour, ", 类型: ", type(time.localtime().tm_hour))
print("时间(分): ", time.localtime().tm_min, ", 类型: ", type(time.localtime().tm_min))
print("时间(秒): ", time.localtime().tm_sec, ", 类型: ", type(time.localtime().tm_sec))

print("\ndatetime模块: ")
print(datetime)
print("\ndatetime.date类: ")
print(datetime.date)
print("日期(datetime.date()(实例初始化)): ", datetime.date(2023, 7, 16), ", 类型: ", type(datetime.date(2023, 7, 16)))
print("日期(datetime.date.today()(类方法初始化)): ", datetime.date.today(), ", 类型: ", type(datetime.date.today()))
print("日期(datetime.date()->标准时间): ", datetime.date.today().ctime(), ", 类型: ",
      type(datetime.date.today().ctime()))
print("日期(datetime.date()->格式化时间): ", datetime.date.today().strftime("%Y-%m-%d %H:%M:%S"), ", 类型: ",
      type(datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")))
print("日期(datetime.date()->标准时间(strftime)): ", datetime.date.today().strftime("%a %b %d %H:%M:%S %Y"), ", 类型: ",
      type(datetime.date.today().strftime("%a %b %d %H:%M:%S %Y")))
print("日期(datetime.date()->时间元组(timetuple)): ", datetime.date.today().timetuple(), ", 类型: ",
      type(datetime.date.today().timetuple()))
print("日期(datetime.date()配合time)",
      time.strptime(datetime.date.today().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"))

print("\ndatetime.time类: ")
print(datetime.time)
print("时间(实例初始化): ", datetime.time(13, 29, 30), ", 类型: ", type(datetime.time(13, 29, 30)))
print("时间(datetime.time()->格式化时间): ", datetime.time(14, 8, 30).strftime("%H:%M:%S"), ", 类型: ",
      type(datetime.time(14, 8, 30).strftime("%H:%M:%S")))

print("\ndatetime.datetime类: ")
print("日期&时间(实例初始化): ", datetime.datetime(2023, 7, 16, 16, 14, 30), ", 类型: ",
      type(datetime.datetime(2023, 7, 16, 16, 14, 30)))
print("日期&时间(类方法初始化): ", datetime.datetime.today(), ", 类型: ", type(datetime.datetime.today()))
print("日期&时间(类方法初始化): ", datetime.datetime.now(), ", 类型: ", type(datetime.datetime.now()))
print("日期&时间(获取日期date): ", datetime.datetime.today().date(), ", 类型: ", type(datetime.datetime.today().date()))
print("日期&时间(获取时间time): ", datetime.datetime.today().time(), ", 类型: ", type(datetime.datetime.today().time()))
print("日期&时间(datetime.datetime()->标准时间): ", datetime.datetime.today().ctime(), ", 类型: ",
      type(datetime.datetime.today().ctime()))
print("日期&时间(datetime.datetime()->格式化时间): ", datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
      ", 类型: ", type(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
print("日期&时间(datetime.datetime()->标准时间(strftime)): ",
      datetime.datetime.today().strftime("%a %b %d %H:%M:%S %Y"), ", 类型: ",
      type(datetime.datetime.today().strftime("%a %b %d %H:%M:%S %Y")))
print("日期&时间(datetime.datetime()->时间元组):", datetime.datetime.today().timetuple(), ", 类型: ",
      type(datetime.datetime.today().timetuple()))
print("日期&时间(格式化时间->时间元组):", datetime.datetime.strptime("2023-07-16 14:23:30", "%Y-%m-%d %H:%M:%S"),
      ", 类型: ", type(datetime.datetime.today().ctime()))
print("日期&时间(格式化时间->时间元组):",
      datetime.datetime.today().strptime("2023-07-16 14:23:30", "%Y-%m-%d %H:%M:%S"), ", 类型: ",
      type(datetime.datetime.today().strptime("2023-07-16 14:23:30", "%Y-%m-%d %H:%M:%S")))
print("日期&时间(datetime.datetime()->时间戳):", datetime.datetime.today().timestamp(), ", 类型: ",
      type(datetime.datetime.today().timestamp()))
print("日期&时间(时间戳->datetime.datetime())", datetime.datetime.fromtimestamp(1689504035.058669), ", 类型: ",
      datetime.datetime.fromtimestamp(1689504035.058669))

print("\ndatetime模块: 获取时间元组元素")
print("datetime.date: 获取时间元组元素")
print("时间(年): ", datetime.date.today().year, ", 类型: ", type(datetime.date.today().year))
print("时间(月): ", datetime.date.today().month, ", 类型: ", type(datetime.date.today().month))
print("时间(日/月): ", datetime.date.today().day, ", 类型: ", type(datetime.date.today().day))

print("\ndatetime.time: 获取时间元组元素")
print("时间(时): ", datetime.time(18, 14, 30).hour, ", 类型: ", type(datetime.time(18, 14, 30).hour))
print("时间(分): ", datetime.time(18, 14, 30).minute, ", 类型: ", type(datetime.time(18, 14, 30).minute))
print("时间(秒): ", datetime.time(18, 14, 30).second, ", 类型: ", type(datetime.time(18, 14, 30).second))
print("时间(毫秒): ", datetime.time(18, 14, 30).microsecond, ", 类型: ", type(datetime.time(18, 14, 30).microsecond))

print("\ndatetime.datetime.today().date(): 获取时间元组元素")
print("时间(年): ", datetime.datetime.today().date().year, ", 类型: ", type(datetime.datetime.today().date().year))
print("时间(月): ", datetime.datetime.today().date().month, ", 类型: ", type(datetime.datetime.today().date().month))
print("时间(日): ", datetime.datetime.today().date().day, ", 类型: ", type(datetime.datetime.today().date().day))

print("\ndatetime.datetime.today().time(): 获取时间元组元素")
print("时间(年): ", datetime.datetime.today().time().hour, ", 类型: ", type(datetime.datetime.today().time().hour))
print("时间(月): ", datetime.datetime.today().time().minute, ", 类型: ", type(datetime.datetime.today().time().minute))
print("时间(日): ", datetime.datetime.today().time().second, ", 类型: ", type(datetime.datetime.today().time().second))

print("\ndatetime.datetime.today(): 获取时间元组元素")
print("时间(年): ", datetime.datetime.today().year, ", 类型: ", type(datetime.datetime.today().year))
print("时间(月): ", datetime.datetime.today().month, ", 类型: ", type(datetime.datetime.today().month))
print("时间(日): ", datetime.datetime.today().day, ", 类型: ", type(datetime.datetime.today().day))
print("时间(时): ", datetime.datetime.today().hour, ", 类型: ", type(datetime.datetime.today().hour))
print("时间(分): ", datetime.datetime.today().minute, ", 类型: ", type(datetime.datetime.today().minute))
print("时间(秒): ", datetime.datetime.today().second, ", 类型: ", type(datetime.datetime.today().second))
print("时间(毫秒): ", datetime.datetime.today().microsecond, ", 类型: ", type(datetime.datetime.today().microsecond))

print("\ndatetime.timedelta类(时间计算-时间间隔): ")
print("支持: datetime.datetime & datetime.timedelta 计算")
print("不支持: time.localtime & datetime.timedelta 计算")
print(datetime.timedelta)
print("时间间隔(天): ", datetime.timedelta(days=1), ", 类型: ", type(datetime.timedelta(days=1)))
print("时间间隔(天): ",
      datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0), ", 类型: ",
      type(datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)))
print("时间计算(1天前): ", datetime.datetime.today() - datetime.timedelta(1))
print("时间间隔(1天前): ", datetime.datetime.today() - datetime.timedelta(days=1))
print("时间间隔(1小时前): ", datetime.datetime.today() - datetime.timedelta(hours=1))
print("时间间隔(1周前): ", datetime.datetime.today() - datetime.timedelta(weeks=1))
print("时间间隔(1周+1天前): ", datetime.datetime.today() - datetime.timedelta(days=1, weeks=1))
print("时间间隔(1周+1天+1小时前): ", datetime.datetime.today() - datetime.timedelta(days=1, weeks=1, hours=1))
# print(time.localtime()-datetime.timedelta(days=1))
birthday = "2000-01-01"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
now_date = datetime.datetime.today().date()
print("datetime-datetime: datetime.timedelta")
day1 = (now_date - birthday_date).days

print("\ndatetime.timezone类: ")
print("")
print(datetime.timezone(datetime.timedelta(hours=1)))

print("\ndatetime.tzinfo类: ")
print(datetime.tzinfo)


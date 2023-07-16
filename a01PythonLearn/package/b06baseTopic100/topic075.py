import datetime


def get_day():
    print("今天的日期：", datetime.datetime.today().strftime("%Y-%m-%d"))
    print("昨天的日期：", (datetime.datetime.today()-datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    print("明天的日期：", (datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    print("一周前的日期：", (datetime.datetime.today()-datetime.timedelta(weeks=1)).strftime("%Y-%m-%d"))

get_day()
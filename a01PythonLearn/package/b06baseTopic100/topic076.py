import datetime


def get_all_date(begin_date: str, end_date: str):
    """
    返回两个日期之间所有的日期
    :param begin_date:
    :param end_date:
    :return:
    """
    date_list = []
    if begin_date <= end_date:
        begin_date_d = datetime.datetime.strptime(begin_date, "%Y-%m-%d").date()
        end_date_d = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        day = (end_date_d - begin_date_d).days
        for d in range(day + 1):
            date_list.append((begin_date_d + datetime.timedelta(days=d)).strftime("%Y-%m-%d"))

    return date_list


def get_all_date_while(begin_date: str, end_date: str):
    """
    返回两个日期之间所有的日期
    :param begin_date:
    :param end_date:
    :return:
    """
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date = (datetime.datetime.strptime(begin_date, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    return date_list


if __name__ == "__main__":
    print(get_all_date("2022-05-12", "2022-05-18"))
    print(get_all_date_while("2022-05-12", "2022-05-18"))

import datetime

birthday = input("请输入生日：")
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
now_date = datetime.datetime.today().date()
day1 = (now_date - birthday_date).days
print(f"你的生日是：{birthday} ，活了 {day1} 天了。")

birthday = input("请输入生日：")
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
now_date = datetime.datetime.today().date()
day2 = (now_date - birthday_date).days
print(f"你的生日是：{birthday} ，活了 {day2} 天了。")

print(f"你比我多活了 {day2-day1} 天")

# coding:utf-8
import datetime
import time

print(datetime.datetime.today())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M-%S"))
print(datetime.datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒"))
print(time.strftime("%Y-%m-%d %H:%M-%S", time.localtime()))

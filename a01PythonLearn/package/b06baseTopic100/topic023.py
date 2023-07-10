
d = {"姓名": "小明", "性别": "男"}
try:
    print(d["性别"])
except KeyError:
    print("字典中没有所选key")


d = {"a": 1, "b": 2, "c": 3}

# 遍历字典是不能修改字典元素，否则会报错RuntimeError: dictionary changed size during iteration
# for mapa in d.keys():
for mapa in list(d.keys()):
    if d[mapa] > 1:
        print(d[mapa])
        d.pop(mapa)
print(d)


# 字典推导式
c = {"a": 1, "b": 2, "c": 3}
b = {x[0]: x[1] for x in c.items() if x[1] <= 1}
# {'a': 1}
print(b)


# 字典推导式
x = {"a": 1, "b": 2, "c": 3}
x = {key: value for key, value in c.items() if value <= 1}
# {'a': 1}
print(x)
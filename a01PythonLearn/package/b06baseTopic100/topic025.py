
d = {"a": 1, "b": 2, "c": 3}
sum_num = 0
for num in d.values():
    sum_num += num
print(sum_num)

# sum可以直接对列表进行求和
print(sum(d.values()))

print(d.values())
print(type(d.values()))
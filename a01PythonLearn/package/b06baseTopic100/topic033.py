
# 计算100之内的偶数和
print(sum([x for x in range(1, 101) if x % 2 == 0]))


sum_value = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum_value += x
print(sum_value)


sum_value = 0
for x in range(1, 101):
    if x % 2 == 1:
        continue
    else:
        sum_value += x
print(sum_value)

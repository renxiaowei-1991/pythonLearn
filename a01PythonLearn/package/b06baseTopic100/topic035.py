
"""
zip
    可以将不同的序列(列表、元组都叫序列)打包在一起
    返回一个个的元组(tuple)，每一个元组中都是被打包序列中的各自的一个元素
"""
a = [1, 2, 3]
b = (4, 5, 6)
for num in range(0, len(a)):
    print(a[num] + b[num])

for i, j in zip(a, b):
    print(i + j)

print(zip(a, b))
print(list(zip(a, b)))
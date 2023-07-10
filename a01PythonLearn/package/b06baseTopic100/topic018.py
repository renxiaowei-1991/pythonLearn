a = ["1", 1, "1", 2]
print(list(set(a)))

b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
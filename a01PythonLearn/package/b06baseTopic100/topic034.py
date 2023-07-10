a = [1, 2, 3]

for x in a:
    print("Item", x, "has index", a.index(x))

for index, item in enumerate(a):
    print("Item", item, "has index", index)

for index, item in enumerate(a):
    print(f"Item {item} has index {index}")

for index, item in enumerate(a):
    print("Item {item} has index {index}".format(item=item, index=index))

tx = "2023-07-09"
print(f"date is {tx}")
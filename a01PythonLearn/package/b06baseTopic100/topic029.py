
from pprint import pprint

dicta = {"a": list(range(1, 11)),
         "b": list(range(11, 21)),
         "c": list(range(21, 31))}
pprint(dicta)

for x in dicta.keys():
    print(x + " has value ", dicta[x])

for key, value in dicta.items():
    print(key, " has value ", value)


"""多级字典"""
from pprint import pprint

d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}


d["employees"][1]["lastName"] = "Smooth"
print(d["employees"][1]["lastName"])
pprint(d["employees"][1]["lastName"])

print(d)
pprint(d)

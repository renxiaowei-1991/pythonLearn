
"""多级字典"""
from pprint import pprint

d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}

pprint(d)
d["employees"].append({"firstName": "Albert", "lastName": "Bert"})
pprint(d)

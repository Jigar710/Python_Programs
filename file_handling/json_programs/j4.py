import json


file = open('out1.txt','r')
d = json.load(file)
print(d)
print(type(d))
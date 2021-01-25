import json
#a = {"name":'sumit',"age":31}
file = open("output.txt","r")
a = json.load(file)
print(a)
print(type(a))
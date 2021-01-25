import json
a = {"name":'sumit',"age":31}
print(type(a))
file = open("output.txt","w")
json.dump(a,file)
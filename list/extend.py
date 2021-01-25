#merge two lists
lst1 = list(range(1,11))
print(lst1)
print(id(lst1))

lst2 = [10,20,30]
print(lst2)
print(id(lst2))
'''
lst3 = lst1 + lst2
print("========After + op=================")
print("lst1 :",lst1)
print("lst2 :",lst2)
print("lst3 :",lst3)
print(id(lst3))
'''
print("=============After extend method==================")
print(id(lst1),id(lst2))
lst1.extend(lst2)
print(lst1)
print(id(lst1))
print(lst2)
print(id(lst2))
'''
print("=============merge using append method==================")

lst3 = []
for i in lst1:
	lst3.append(i)
for i in lst2:
	lst3.append(i)
print(lst1)
print(lst2)
print(lst3)

lst1.append(lst2)
print(lst1)
print(lst2)
'''
lst = list(range(1,11))
print(lst)

#lst1 = lst
lst1 = lst.copy()
print(id(lst),id(lst1))
print(lst)
print(lst1)

lst[0] = 100
print(lst)
print(lst1)

lst1[0] = 999
print(lst)
print(lst1)
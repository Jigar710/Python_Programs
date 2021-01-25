lst1 = [5,1,2,3,4,5]

lst2 = lst1
print(lst1)
print(lst2)

lst1[0] = 999
print(lst1)
print(lst2)

print(id(lst1))
print(id(lst2))

lst3 = lst1.copy()

print(id(lst1))
print(id(lst3))

print(lst1)
print(lst3)

lst1[0]=1000
print(lst1)
print(lst3)
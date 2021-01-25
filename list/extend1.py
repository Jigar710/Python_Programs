#merge two lists into third list without using + operator

lst1 = list(range(1,11))
print(lst1)
print(id(lst1))

lst2 = [10,20,30]
print(lst2)
print(id(lst2))

lst3 = []
lst3 = lst1.copy()
lst3.extend(lst2)

print(lst1)
print(lst2)
print(lst3)
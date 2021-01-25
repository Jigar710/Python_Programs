lst = list(range(1,11))
print(lst)
print(id(lst))

lst.clear()
print(lst)
print(id(lst))

print("==============del method=============")
lst = list(range(1,11))
print(id(lst))
print(lst)

del lst
print(id(lst))
print(lst)
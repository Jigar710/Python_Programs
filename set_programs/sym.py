a = {1,2,3,4,5}
b = {4,5,6,7}

c = a.symmetric_difference(b)
print(a)
print(b)
print(c)

a.symmetric_difference_update(b)
print(a)
print(b)

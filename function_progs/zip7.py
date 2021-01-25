d1 = {'a':1,'b':2,'c':3}
d2 = {'aa':10,'bb':22,'cc':33}
print(d1)
print(*d1)

lst1 = [1,2,3,4,5]
print(lst1)
print(*lst1)

z = zip(d1,d2)
print(list(z))

z = zip(d1.items(),d2.items())
print(list(z))
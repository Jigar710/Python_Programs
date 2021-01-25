d1 = {'a':1,'b':2,'c':3}
lst = [10,20,30]

z = zip(d1,lst)
print(list(z))

z = zip(d1.items(),lst)
print(list(z))
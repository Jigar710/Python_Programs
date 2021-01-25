
lst1 = [1,2,3,4,5]
lst2 = [10,20,30,40]

z = zip(lst1,lst2)
l = list(z)

l1,l2 = zip(*l)
print(l1)
print(l2)

#unzip dictionary [(key),(value)]
d = {'a':1,'b':2,'c':3}
print(d)
l1 = zip(*d.items())
print(list(l1))

#store key n values in diff list
d = {'a':1,'b':2,'c':3}
print(d)
k,v=zip(*d.items())
print(list(k))
print(list(v))

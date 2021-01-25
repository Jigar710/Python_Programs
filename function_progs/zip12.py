lst1 = [1,2,3,4,5]
lst2 = [10,20,30,40]

z = zip(lst1,lst2)
l = list(z)

l1,l2 = zip(*l)
print(l1)
print(l2)

d = {'a':1,'b':2,'c':3}
l1 = zip(*d)
print(list(l1))
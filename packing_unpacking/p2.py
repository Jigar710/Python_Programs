#lst = [1,2,3,4,5]
lst = (1,2,3,4,5)

a,b,*c = lst
print(a)
print(b)
print(c,type(c))

a,*b,c = lst
print(a)
print(b)
print(c)

a,b,*c,d = lst
print(a)
print(b)
print(c)
print(d)

#a,*b,c,*d,e = lst # not allowed
#a,b,c = lst[0:5:2]
a,b,c = lst[::2]
print(a)
print(b)
print(c)

*a,b,c = lst
print(b,c)
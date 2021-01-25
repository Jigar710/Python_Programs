'''
lst = [1,2,3,4,5]
a,b,c,d,e = lst
print(a,b,c,d,e)
a,b,*c = lst
print(a,b,c)
a,*b,c = lst
print(a,b,c)
*a,b,c = lst
print(a,b,c)
'''

lst = [1,2,3]
a,b,c,*d = lst
print(a,b,c,d)
a,b,*c,d = lst
print(a,b,c,d)
*a,b,c,d = lst
print(a,b,c,d)

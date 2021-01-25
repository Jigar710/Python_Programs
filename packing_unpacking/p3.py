#unpacking
lst = [1,2,3,4,5]
print(lst)

a = 10
b = 20
print(a,b)

print(*lst)

a,b,c,d,e = lst
print(a,b,c,d,e)
#============================================================================================
'''
lst = [1,2,3,4]
l1 = lst
a,b,*c = lst #unpacking
#*c : use for packing
print(lst)
print(*lst)#unpacking
'''
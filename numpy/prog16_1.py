import numpy as np

lst = [['joe',80,90,70],['will',10,20,66],['Bob',100,20,100]]
ar1 = np.array(lst)
print(ar1)
print(ar1 == 'Bob')

print(ar1[ar1 == 'Bob'])


#names = ar1[::][0]
names = ar1[::,0]
print(names)

print(ar1[names=='Bob'])

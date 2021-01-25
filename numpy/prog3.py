import numpy as np
'''
#data1 = [6,7.5,8,9,1]
#data1 = [6,7.5,8,9,1,'hi']
#data1 = (6,7.5,8,9,1)
#data1 = {1,2,3,4}
data1 = {'a':1,'b':2,'c':3,'d':4}
data1 = list(data1.items())
arr1 = np.array(data1)
print(arr1,type(arr1))
print(arr1.shape)
print(arr1.dtype)
print(arr1.ndim)

#data2 = [[1,2,3,4],[5,6,7,8]]
data2 = [[1,2,3,4],[5,6,7,8,9]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)

lst = [1,2,3]
#lst = [1,2,3,'hi']
d = np.array(lst,dtype='float32')
print(d)
print(d.dtype)
'''
lst = [1,2,3,4.4,90.9]

d = np.array(lst)
#d = np.array(lst,dtype='int32')
print(d)
print(d.dtype)
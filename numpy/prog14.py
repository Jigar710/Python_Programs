import numpy as np

arr = np.arange(10)

#print(arr)
arr[5:8] = 12
#print(arr)

arr_slice = arr[5:8]
#print(arr_slice)

arr_slice[1] = 12345
#print(arr_slice)
print(arr)

arr_slice[:] = 64
#print(arr_slice)
print(arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
'''
print(arr2d[2])
print(type(arr2d[2]))
print(arr2d[0][2])
print(arr2d[0,2])
'''
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
#print(arr3d[0])

print(arr)
print(arr[1:6])

print(arr2d)
print(arr2d[:2])

print(arr2d[:2,:1])
print(arr2d[1,:2])

print()

print(arr2d[:2,2])
print(arr2d[:2,:2])

print(arr2d[:,:1])

arr2d[:2,1:] = 0
print(arr2d)
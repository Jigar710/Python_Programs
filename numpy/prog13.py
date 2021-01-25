import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)

print(arr2d[2])
print(type(arr2d[2]))
print(arr2d[0][2])
print(arr2d[0,2])
print(arr2d.shape)

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d.shape)

print(arr3d[1,0])
print(arr3d[1,0,2])

print(arr3d * 2)

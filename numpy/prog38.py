import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
print(arr1)
print(arr2)
print("-------------------------------")
print(np.concatenate([arr1,arr2],axis=0))
print(np.concatenate([arr1,arr2],axis=1))

print("-------------------------------")
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
print(np.column_stack((arr1,arr2)))
print(arr1[:,np.newaxis])
print(arr1[np.newaxis])

help
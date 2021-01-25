import numpy as np

arr = np.arange(8)
print(arr)
arr1 = arr.reshape((4,2))
print(arr)
print(arr1)

print(arr.reshape((4,2)).reshape((2,4)))

arr = np.arange(15)
arr1 = arr.reshape((5,-1))
print(arr1)
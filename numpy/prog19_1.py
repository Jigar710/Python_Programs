import numpy as np

arr = np.zeros(16).reshape((4,4))
print(arr)
arr[::2,::2] = 1
arr[1::2,1::2] = 1
print(arr)

arr = np.arange(1,17).reshape((4,4))
print(arr)

arr[[0,-1],[0,-1]] = 0
print(arr)

arr = np.arange(1,17).reshape((4,4))
print(arr)

arr[[0,0,-1,-1],[0,-1,0,-1]] = 0
print(arr)

arr = np.arange(1,17).reshape((4,4))
print(arr)

arr[[0,-1]] = 0
arr[:,[0,-1]]=0
print(arr)
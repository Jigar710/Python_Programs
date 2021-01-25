import numpy as np

arr = np.arange(1,37).reshape(6,6)
#print(arr)

arr[1:-1,1:-1] = 0
print(arr)
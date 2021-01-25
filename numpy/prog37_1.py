import numpy as np

arr = np.arange(15)

other_arr = np.ones((3,5))
print(other_arr.shape)
print(arr.reshape(other_arr.shape))

arr = np.arange(10).reshape((5,2))
print(arr)
#ar1 = arr.ravel()
ar1 = arr.flatten()
ar1[0] = 100
print(arr)
print(ar1)

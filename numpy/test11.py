import numpy as np

my_arr = np.arange(10)
print(my_arr)

my_arr = np.arange(2,10)
print(my_arr)

my_arr = np.arange(2,10,2)
print(my_arr)

my_arr = np.arange(10,2,-1)
print(my_arr)

my_arr = np.arange(9,2,-1)
print(my_arr)

print(type(my_arr))
print(my_arr.shape)

my_arr = np.arange(9).reshape(3,3)
print(my_arr)
print(my_arr.shape)
print(my_arr.dtype)
print(my_arr.ndim)

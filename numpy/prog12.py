import numpy as np

arr = np.arange(10)

print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
#arr_slice = arr[5:8].copy()
print(arr_slice)

arr_slice[1] = 12345
print(arr_slice)
print(arr)

arr_slice[:] = 64
print(arr_slice)
print(arr)



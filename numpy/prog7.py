import numpy as np
#[0 1 2 3 4 5 6 7 8 9]
arr = np.arange(10)

print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
#[ 0  1  2  3  4 12 12 12  8  9]
print(arr)

arr_slice = arr[5:8]
#[12 12 12]
#arr_slice = arr[5:8].copy()
#arr_slice = np.array(arr[5:8])
print(arr_slice,type(arr_slice))

arr_slice[1] = 12345
#[   12 12345    12]
print(arr_slice)
print(arr)
#[ 0  1   2 3 4    12 12345    12 8 9]
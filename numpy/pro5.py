import numpy as np

#arr1 = np.array([1,2,3],dtype=np.float64)
arr1 = np.array([1,2,3],dtype='float64')
arr1 = np.array([1,2,3],dtype='d')
arr2 = np.array([1,2,3],dtype=np.int32)

print(arr1,arr1.dtype)
print(arr2,arr2.dtype)

arr3 = np.array([1,2,3,4,5])
print(arr3,arr3.dtype)

#float_arr = arr3.astype(np.float64)
float_arr = arr3.astype(arr1.dtype)
print(float_arr,float_arr.dtype)

arr4 = np.array([2,3,4.4,2.3])
print(arr4,arr4.dtype)
print(arr4.itemsize)

int_arr = arr4.astype(np.int32)
print(int_arr,int_arr.dtype)
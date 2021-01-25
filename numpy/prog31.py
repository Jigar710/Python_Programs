import numpy as np

arr = np.random.randn(4)
print(arr)
arr.sort()
print(arr)

print("--------------------")

arr = np.random.rand(4,3)
print(arr)
#arr.sort(0)	# column-wise sorting (column-data)
arr.sort(1)# row-wise sorting (row-data)
#arr.sort(axis=1)# row-wise sorting (row-data)
print(arr)

print("--------------------")
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05*len(large_arr))])
#print(large_arr)

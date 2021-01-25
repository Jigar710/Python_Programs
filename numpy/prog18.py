#fancy indexing
import numpy as np

arr = np.empty((8,4))
print(arr)
for i in range(len(arr)):
	arr[i] = i
	
print(arr)

print(arr[[4,3,0,6]])
print(arr[[-3,-5,-7]])

import numpy as np

arr = np.arange(32).reshape((8,4))
'''
print(arr)
print('arr[[1,5,7,2],[0,3,1,2]]')
print(arr[[1,5,7,2],[0,3,1,2]])
#print(arr[[1,5,7,2],[0,3,1]])#error
print(arr[[1,5,7,2]][:,[0,3,1]])
print(arr[[1,5,7,2]])
'''
print(arr)
print("===============")
print(arr[[1,5,7,2]][:,[0,3,1]][[1,2]])
#print(x[[1,2]])

print("===============")

a1 = arr[[1,5,7,2]]
print(a1)
print(a1[:,[0,3,1]])








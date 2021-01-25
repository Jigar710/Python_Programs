'''
Write a NumPy program to create a 2d array with 1 on the border and 0 inside.  
Expected Output:
Original array:
[[ 1. 1. 1. 1. 1.]
...................
[ 1. 1. 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 1. 1. 1. 1. 1.]
...................
[ 1. 1. 1. 1. 1.]]
'''
import numpy as np
ar = np.zeros((6,5))
print(ar)
print("------------------------")
ar[[0,-1]]=1
ar[:,[0,-1]]=1

print(ar)

print("------------------------")
ar = np.ones((6,5))
print(ar)
ar[1:-1,1:-1] = 0
print(ar)

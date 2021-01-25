'''
Write a NumPy program to find the indices of the maximum and minimum
values along the given axis of an array.
Original array: [1 2 3 4 5 6]
Maximum Values: 5
Minimum Values: 0
'''
import numpy as np
ar1 = np.arange(10)
print(ar1)
print(np.argmin(ar1))
print(np.argmax(ar1))

#ar2 = np.array([2,3,1,22,32,4,55,32])
ar2 = np.array([2,3,1,22,32,4,55,32,1])
print(ar2)
print(np.argmin(ar2))
print(np.argmax(ar2))

ar3 = np.array([2,3,1,22,32,4,55,32]).reshape(4,2)

print(ar3)
print(np.argmin(ar3))
print(np.argmax(ar3))
print(np.argmin(ar3,axis=1))
print(np.argmax(ar3,axis=1))


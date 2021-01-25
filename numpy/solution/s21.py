'''
Write a NumPy program to find the set exclusive-or of two arrays. 
Set exclusive-or will return the sorted, unique values that are in only one 
(not both) of the input arrays.  
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70]
Unique values that are in only one (not both) of the input arrays:
[ 0 20 30 50 60 70 80]
'''
import numpy as np
ar1 = np.array([0,10,20,40,60,80])
ar2 = np.array([10,30,40,50,70])

print(ar1)
print(ar2)

print(np.setxor1d(ar1,ar2))
print("========================")
ar1 = np.array([0,10,20,40,60,80,4,3,9])
ar2 = np.array([10,30,40,50,70])

print(ar1)
print(ar2)

print(np.setxor1d(ar1,ar2))
'''
Write a NumPy program to find common values between two arrays.  
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [10, 30, 40]
Common values between two arrays:
[10 40]
'''
import numpy as np
ar1 = np.array([0,10,20,40,60])
ar2 = np.array([10,30,40])
print(ar1)
print(ar2)
ar3 = np.intersect1d(ar1,ar2)
print(ar3)
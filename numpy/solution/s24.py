'''
Write a NumPy program to test whether any array element along a given axis 
evaluates to True.  
Note: 0 evaluates to False in NumPy.
'''
import numpy as np
ar1 = np.array([True,True])
print(np.any(ar1))
ar1 = np.array([True,False])
print(np.any(ar1))
ar1 = np.array([True,100])
print(np.any(ar1))
ar1 = np.array([0,100])
print(np.any(ar1))
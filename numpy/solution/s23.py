'''
Write a NumPy program to test whether all elements in an array evaluate to True.  
Note: 0 evaluates to False in NumPy.
'''
import numpy as np
ar1 = np.array([True,True])
print(np.all(ar1))
ar1 = np.array([True,False])
print(np.all(ar1))
ar1 = np.array([True,100])
print(np.all(ar1))
ar1 = np.array([0,100])
print(np.all(ar1))
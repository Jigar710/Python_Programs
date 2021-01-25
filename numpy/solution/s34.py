'''
Write a NumPy program to create an array of ones and an array of zeros.
Expected Output:
Create an array of zeros
Default type is float
[[ 0. 0.]]
Type changes to int
[[0 0]]
Create an array of ones
Default type is float
[[ 1. 1.]]
Type changes to int
[[1 1]]
'''
import numpy as np
print("Create an array of zeros")
x = np.zeros((1,2))
print("Default type is float")
print(x)
print("Type changes to int")
x = np.zeros((1,2), dtype = np.int)
print(x)
print("Create an array of ones")
y= np.ones((1,2)) 
print("Default type is float")
print(y)
print("Type changes to int")
y = np.ones((1,2), dtype = np.int)
print(y)
'''
Write a NumPy program to create a 2-dimensional array of size 2 x 3 (composed of 
4-byte integer elements), also print the shape, type and data type of the array. 
Expected Output:

(2, 3)
int32
'''
import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(type(x))	
print(x.shape)
print(x.dtype)
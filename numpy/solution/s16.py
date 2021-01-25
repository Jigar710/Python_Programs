'''
Write a NumPy program to find the number of elements of an array, length of one array 
element in bytes and total bytes consumed by the elements.  
Expected Output:
Size of the array: 3
Length of one array element in bytes: 8
Total bytes consumed by the elements of the array: 24
'''
import numpy as np
ar = np.arange(1,4)
print(ar)
print(len(ar))
print(ar.itemsize)
print(len(ar) * ar.itemsize)
print(ar.nbytes)
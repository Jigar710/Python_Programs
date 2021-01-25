'''
Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.  
Checkerboard pattern:
[[0 1 0 1 0 1 0 1]
..........
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]]
'''
import numpy as np
ar = np.zeros((8,8),dtype='int')
print(ar)
ar[::2,::2] = 1
ar[1::2,1::2] = 1
print(ar)
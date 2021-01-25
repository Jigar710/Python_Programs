'''
Write a NumPy program to construct an array by repeating.  
Sample array: [1, 2, 3, 4]
Expected Output:
Original array
[1, 2, 3, 4]
Repeating 2 times
[1 2 3 4 1 2 3 4]
Repeating 3 times
[1 2 3 4 1 2 3 4 1 2 3 4]
'''
import numpy as np
ar1 = np.array([1, 2, 3, 4])
print(ar1)
ar2 = np.tile(ar1,2)
print(ar2)
ar3 = np.tile(ar1,3)
print(ar3)
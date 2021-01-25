'''
Write a NumPy program to repeat elements of an array.
Expected Output:
[3 3 3 3]
[1 1 2 2 3 3 4 4]
'''
import numpy as np
ar1 = np.repeat(3,4)
print(ar1)
x = np.array([[1,2],[3,4]])
ar2 = np.repeat(x,2)
print(ar2)

'''
Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.  
Expected Output:
[[ 2 3 4]
[ 5 6 7]
[ 8 9 10]]
 
'''
import numpy as np
ar = np.arange(2,11).reshape(3,3)
print(ar)
'''
 Write a NumPy program to create a null vector of size 10 and update sixth value to 11. 
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Update sixth value to 11
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
'''
import numpy as np
ar1 = np.zeros(10)
print(ar1)
ar1[5] = 11
print(ar1)
'''
Write a NumPy program to convert an array to a float type.  
Sample output:
Original array
[1, 2, 3, 4]
Array converted to a float type:
[ 1. 2. 3. 4.]
 '''
 
import numpy as np
ar = np.arange(1,5)
print(ar)
ar1 = ar.astype(dtype='float')
print(ar1)
ar2 = np.asfarray(ar)
print(ar2)
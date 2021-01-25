'''
Write a NumPy program to find the real and imaginary parts of an array of complex numbers.  
Expected Output:
Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
Real part of the array:
[ 1. 0.70710678]
Imaginary part of the array:
[ 0. 0.70710678]
'''
import numpy as np
ar1 = np.array([ 1.00000000+0.j,0.70710678+0.70710678j])
print(ar1)
ar2 = ar1.real
print(ar2)
ar3 = ar1.imag
print(ar3)
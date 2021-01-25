'''
Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees.
Centigrade values are stored into a NumPy array.  
Sample Array [0, 12, 45.21 ,34, 99.91]
Expected Output:
Values in Fahrenheit degrees:
[ 0. 12. 45.21 34. 99.91]
Values in Centigrade degrees:
[-17.77777778 -11.11111111 7.33888889 1.11111111 37.72777778]

Formula : c = (5 * (F - 32))/9
		: F = (9 * C + 32 * 5)/5
'''
import numpy as np
ar1 = np.array([0, 12, 45.21 ,34, 99.91])
ar2 =  (5 * ar1 - 32* 5 )/9
print(ar2)
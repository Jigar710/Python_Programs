'''
Write a NumPy program to append values to the end of an array.  
Expected Output:
Original array:
[10, 20, 30]
After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]
'''
import numpy as np
ar = np.array([10, 20, 30])
print(ar)
ar = np.append(ar,[40,50,60,70,80,90])
print(ar)
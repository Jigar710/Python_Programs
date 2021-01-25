'''
Write a NumPy program to get the unique elements of an array.  
Expected Output:
Original array:
[10 10 20 20 30 30]
Unique elements of the above array:
[10 20 30]
Original array:
[[1 1]
[2 3]]
Unique elements of the above array:
[1 2 3]
'''
import numpy as np
ar1 = np.array([10,10,20,20,30,30])
print(ar1)
print(np.unique(ar1))
ar2 = np.array([[1,1],[2,3]])
print(ar2)
print(np.unique(ar2))
'''
Write a NumPy program to create a new array of 3*5, filled with 2. 
Expected Output:
[[2 2 2 2 2]
[2 2 2 2 2]
[2 2 2 2 2]]
[[2 2 2 2 2]
[2 2 2 2 2]
[2 2 2 2 2]]
'''
import numpy as np
#using no.full
x = np.full((3, 5), 2, dtype=np.uint)
print(x)
#using no.ones
y = np.ones([3, 5], dtype=np.uint) *2
print(y)
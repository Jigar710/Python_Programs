'''
Write a NumPy program to sort an along the first, last axis of an array.
Sample array: [[2,5],[4,4]]
Expected Output:
Original array:
[[4 6]
[2 1]]
Sort along the first axis:
[[2 1]
[4 6]]
Sort along the last axis:
[[1 2]
[4 6]]
'''
import numpy as np
ar = np.array([[4,6],[2,1]])
print(ar)
x = np.sort(ar,axis=0)
print(x)
y = np.sort(x,axis=1)
print(y)
'''
Write a NumPy program to get the values and indices of the elements that are bigger than 
10 in a given array.   
Original array: [[ 0 10 20] [20 30 40]] 
Values bigger than 10 = [20 20 30 40] 
Their indices are (array([0, 1, 1, 1]), array([2, 0, 1, 2])) 
'''
import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values bigger than 10 =", x[x>10])
print("Their indices are ", np.nonzero(x > 10))
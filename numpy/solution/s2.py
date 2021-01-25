'''
Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.  
Expected Output:
Original List: [12.23, 13.32, 100, 36.32]
One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
'''
import numpy as np
 
lst = [12.23, 13.32, 100, 36.32]
ar = np.array(lst)
print(ar)
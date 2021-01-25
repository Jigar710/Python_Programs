'''
Write a NumPy program to find the set difference of two arrays. 
The set difference will return the sorted, unique values in array1 that are not in array2.  
Expected Output:
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70, 90]
Set difference between two arrays:
[ 0 20 60 80]
'''
import numpy as np
ar1 = np.array([0,10,20,40,60,80])
ar2 = np.array([10,30,40,50,70,90])
print(ar1)
print(ar2)
print(np.setdiff1d(ar1,ar2))
print("================================")
ar1 = np.array([[0,10,20],[40,60,80]])
ar2 = np.array([[10,30,40],[50,70,90]])
print(ar1)
print(ar2)
print(np.setdiff1d(ar1,ar2))
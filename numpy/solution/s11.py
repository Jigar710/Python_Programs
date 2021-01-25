'''
Write a NumPy program to convert a list and tuple into arrays.  
List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
[1 2 3]]
'''
import numpy as np

lst = [1,2,3,4,5,6,7,8]
ar1 = np.array(lst)
#ar1 = np.asarray(lst)
print(ar1)

t = ([8,4,6],[1,2,3])
ar2 = np.array(t)
#ar2 = np.asarray(t)

print(ar2)
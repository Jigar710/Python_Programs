'''
Write a NumPy program compare two given arrays.
Array a: [1 2]
Array b: [4 5]
a > b
[False False]
a >= b
[False False]
a < b
[ True True]
a <= b
[ True True]
'''
import numpy as np
ar1 = np.array([1,2])
ar2 = np.array([4,5])

print(ar1>ar2)
print(ar1>=ar2)
print(ar1<ar2)
print(ar1<=ar2)
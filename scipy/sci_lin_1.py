from scipy.linalg import *
import numpy as np
'''
x + 2y + 3z = 1
4x + 5y + 6z = 2
7x + 8y + 9z = 3

Ax = B
'''

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([1,2,3])

print(a)
print(b)

print(type(a))
print(type(b))


x = solve(a,b)			# Ax = B ==> x = A^(-1)B
print(x,end="\n\n\n")


# check

c = a.dot(x) - b
print(c)

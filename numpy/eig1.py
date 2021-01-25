import numpy as np
from numpy import linalg as LA

a = np.array([[1,-2],[-5,4]])
print(a)

w,v = LA.eig(a)
print(w)
print(v)

a = np.array([[2,2,1],[1,3,1],[1,2,2]])
w,v = LA.eig(a)
print(w)
print(v)
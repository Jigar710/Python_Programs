from numpy import *
from scipy.linalg import *

A = random.rand(3,3)
B = random.rand(3,3)

print(A)
print(B)

x = solve(A,B) # AX = B ==> X = A^(-1)B

print(x)

C = A.dot(x) - B
print(C)

print(norm(C))
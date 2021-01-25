from scipy import *
from numpy import *
from scipy.linalg import *

A = random.rand(3,3)

print(A)
ans = det(A)
print(ans)

B = inv(A)
print(B)

print("========================================")
print(A)
a = norm(A,ord=1)	# col sum max
b = norm(A,ord=2)	# max of sum(aij)2
c = norm(A,ord=Inf)	# row sum max

print(a)
print(b)
print(c)
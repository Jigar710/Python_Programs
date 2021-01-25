from scipy import *
from numpy import *
from scipy.linalg import *

A = random.rand(3,3)

evals = eigvals(A)
print(evals)

evals,evecs = eig(A)
print(evals)
print(evecs)


n = 1
#c = dot(A,evecs[:,n])-evals[n] * evecs[:,n]
c = dot(A,evecs[:,n])-evals[n] * evecs[:,n]
print(c)
print(norm(c))

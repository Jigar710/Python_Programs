from scipy.sparse import *
from numpy import *

A = lil_matrix((4,4))
print(A)

A[0,0] = 1
A[1,1] = 3
A[2,2] = A[2,1] = 1
A[3,3] = A[3,0] = 1

print(A)
print(A.todense())
B = A.todense()

C = csc_matrix(B)
#B = csr_matrix(A)
print(C)
print(C.todense())
from numpy import *
from scipy.sparse import *

A = lil_matrix((4,4))
print(A)

#M = array([[1,0,0,0],[0,3,0,0],[0,1,1,0],[1,0,0,1]])

A[0,0] = 1
A[1,1] = 3
A[2,1] = A[2,2] = 1
A[3,0] = A[3,3] = 1

print(A)
print(type(A))

B = A.todense()
print(B)

B = csr_matrix(A)
#B = csc_matrix(A)
print(B)
print(B.todense())
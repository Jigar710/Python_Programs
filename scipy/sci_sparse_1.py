from scipy.sparse import *
from numpy import *

#dense matrix
M = array([[1,0,0,0],[0,3,0,0,],[0,1,1,0],[1,0,0,1]])
print(M)

#A = csr_matrix(M)
#A = lil_matrix(M)
A = coo_matrix(M)
print(A)
print(type(A))

M = A.todense()
print(M)
print(type(M))

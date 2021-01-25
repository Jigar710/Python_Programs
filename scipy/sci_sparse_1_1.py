from scipy.sparse import *
from numpy import *

#dense matrix
M = array([[1,0,0,0],[0,3,0,0,],[0,1,1,0],[1,0,0,1]])
print(M)

A = csr_matrix(M)
print(A,type(A))
print(A.tocoo())
print(A.tolil())
M = A.todense()
print(M)

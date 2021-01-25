from scipy.sparse import *
from scipy import *
from numpy import *

#dense matrix
M1 = array([[1,0,0,0],[0,3,0,0,],[0,1,1,0],[1,0,0,1]])
M2 = array([[0,1,0,0],[0,3,0,0,],[0,1,1,0],[1,0,0,1]])


#A = csr_matrix(M)
#A = lil_matrix(M)
A = coo_matrix(M1)
B = coo_matrix(M2)

C = A + B
M3 = M1 + M2

print(C.todense())
print(M3)
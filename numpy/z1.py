import numpy as np

ar1 = np.zeros(10)
print(ar1)

ar2 = np.zeros((2,3))
print(ar2)
print(len(ar2))
print(ar2[0],type(ar2[0]))

ar2 = np.zeros((2,3),dtype='int8')
print(ar2)

ar2 = np.zeros((2,3),dtype='str')
print(ar2)

ar2 = np.arange(9,dtype='float32')
print(ar2)

ar3 = np.zeros_like(ar2)
print(ar3,ar3.dtype)
print(len(ar3))
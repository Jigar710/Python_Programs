import numpy as np

ar1 = np.arange(9,dtype='int16').reshape(3,3)
print(ar1)

print(ar1[0])
print(ar1[1])
print(ar1[2])
#print(ar1[3])

print(ar1[-1])

print(ar1[0:])
print(ar1[:1])
print(ar1[0::2])

print(ar1[::-1])

print(ar1[0][0])
print(ar1[0][:])
print(ar1[0,0])
print(ar1[0,1])
print(ar1[0][1])
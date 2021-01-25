import numpy as np

a = np.zeros(10,dtype=int)
print(a,a.dtype)

b = np.zeros((3,6))
print(b)

c = np.ones((2,3))
print(c)

d = np.empty((2,3,2))
print(d)

e = np.arange(9)
print(e)
print(e.dtype)

e = np.arange(2,9)
print(e)
print(e.dtype)

e = np.arange(1,9,2)
print(e)
print(e.dtype)

e = np.arange(5,1,-1,dtype='float')
print(e)
print(e.dtype)


ar = np.zeros(5,dtype=complex)
print(ar)
ar = np.ones(5,dtype=complex)
print(ar)
ar = np.empty(5,dtype=complex)
print(ar)

#ar = np.full(5,10+2j,dtype=float)
ar = np.full(5,10+2j,dtype=complex)
print(ar)
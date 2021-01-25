import numpy as np
from numpy.linalg import inv,qr

X = np.random.rand(3,3)

mat = X.T.dot(X)
print(mat)


print(inv(mat))
print(mat.dot(inv(mat)))

q,r = qr(mat)
print("--------------------------------")
print(mat)
print(q)
print(r)

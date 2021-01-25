import numpy as np
from scipy import linalg

a = np.random.rand(3,2)

U,s,Vh = linalg.svd(a)

print(U)
print(s)
print(Vh)
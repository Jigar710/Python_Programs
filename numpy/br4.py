import numpy as np

ar1 = np.arange(1,4).reshape(1,3)
print(ar1)

ar2 = np.arange(1,4).reshape(3,1)
print(ar2)

ar3 = ar1 + ar2
print(ar3)
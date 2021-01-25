#find cumsum
import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

print(np.cumsum(ar))
print(np.cumsum(ar,axis = 1))
print(np.cumsum(ar,axis = 0))

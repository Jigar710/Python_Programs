#find cumprod
import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

print(np.cumprod(ar))
print(np.cumprod(ar,axis = 1))
print(np.cumprod(ar,axis = 0))

#find mean
import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

print(np.mean(ar))
print(np.mean(ar,axis = 1))
print(np.mean(ar,axis = 0))

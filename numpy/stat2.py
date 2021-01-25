#find sum
import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

print(np.sum(ar))
print(np.sum(ar[0]))
print(np.sum(ar[:,0]))
print(np.sum(ar,axis = 1))
print(np.sum(ar,axis = 0))

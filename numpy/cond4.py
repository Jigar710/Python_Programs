import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

ar = np.where(ar%2,-1,ar)
print(ar)
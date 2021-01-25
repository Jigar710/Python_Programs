import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

ar = ar>0
print(ar)
print(np.sum(ar))
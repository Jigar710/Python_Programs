import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

print(ar%2)
#ar[ar % 2] = 0
ar[ar % 2==0] = 0
print(ar)
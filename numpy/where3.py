#extract elements from a given range
import numpy as np

a = np.arange(15)

# Method 1
index = np.where((a >= 5) & (a <= 10))
print(a[index])

# Method 2:
index = np.where(np.logical_and(a>=5, a<=10))
print(a[index])


# Method 3: (thanks loganzk!)
print(a[(a >= 5) & (a <= 10)])
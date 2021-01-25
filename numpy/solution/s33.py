'''
Write a NumPy program to find the memory size of a NumPy array.
'''
import numpy as np
n = np.zeros((4,4))
print("%d bytes" % (n.size * n.itemsize))
print(n.nbytes)
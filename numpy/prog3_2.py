import numpy as np

lst = [1,2,3,4,5]

ar1 = np.asarray(lst)
print("\nbefore changes...")
print(lst)
print(ar1)

lst[0] = 100
print("\nafter changes in lst...")
print(lst)
print(ar1)

ar1[0] = 999
print("\nafter changes in ndarray...")
print(lst)
print(ar1)
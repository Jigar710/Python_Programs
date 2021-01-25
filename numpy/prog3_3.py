import numpy as np

lst = [1,2,3,4,5]

ar1 = np.array(lst)
print("data of ndarray...")
print(ar1)

ar2 = np.array(ar1)
ar2[0] = 100
print("\nafter change in new ndarray created using array...")
print(ar1)
print(ar2)

ar3 = np.asarray(ar1)
ar3[0] = 100
print("\nafter change in new ndarray created using asarray...")
print(ar1)
print(ar3)
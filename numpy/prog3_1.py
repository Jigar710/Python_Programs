import numpy as np

lst = [1,2,3,4,5]

ar1 = np.array(lst)
print("before modify...")
print(lst)
print(ar1)

print("\nafter modify lst")
lst[0] = 100
print(lst)
print(ar1)

print("\nafter modify ndarray")
ar1[0] = 999
print(lst)
print(ar1)
# pip3 install numpy

import numpy as np
import time

my_arr = np.arange(1000000)
my_list = list(range(1000000))

t1 = time.time()

for _ in range(10): my_arr2 = my_arr * 2

t2 = time.time()

for _ in range(10): my_list2 = [x * 2 for x in my_list]

t3 = time.time()

print((t2 - t1) * 1000)
print((t3 - t2) * 1000)

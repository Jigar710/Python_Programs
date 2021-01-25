'''
Write a NumPy program to create an empty and a full array.  
Expected Output:
[ 6.93270651e-310 1.59262180e-316 6.93270559e-310 6.93270665e-310]
[ 6.93270667e-310 6.93270671e-310 6.93270668e-310 6.93270483e-310]
[ 6.93270668e-310 6.93270671e-310 6.93270370e-310 6.93270488e-310]]
[[6 6 6]
[6 6 6]
[6 6 6]]
'''
import numpy as np
ar1 = np.empty((3,4))
print(ar1)
ar2 = np.full((3,3),6)
print(ar2)
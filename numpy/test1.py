import numpy as np
a=[256,2,0,4,-5]
ar = np.array(a,dtype='uint8')
print(ar)
'''
-5 : total range 
0 to 255

-5  -4  -3  -2  -1  0
251	252	253	254	255
'''

ar1 = np.array(a,dtype='bool')
print(ar1)
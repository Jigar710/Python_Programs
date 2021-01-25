from scipy import optimize
from scipy.fftpack import dct,idct
import numpy as np

ar = np.array([4.,3.,5.,10.,5.,3.])
y = dct(ar,norm="ortho")
print(y)

yinv = idct(y,norm='ortho')
print(yinv)

import numpy as np
from scipy.interpolate import *
import matplotlib.pyplot as plt

x = np.linspace(0,4,12)
y = np.cos(x**2/3+4)
'''
print(x,y)

plt.plot(x,y,'o')
plt.show()
'''

#f1 = interp1d(x,y,kind='linear')
#f1 = interp1d(x,y,kind='nearest')
#f2 = interp1d(x,y,kind='cubic')

f1 = interp1d(x,y,kind="previous")
f2 = interp1d(x,y,kind="next")

xnew = np.linspace(0,4,30)

plt.plot(x,y,'o',xnew,f1(xnew),'-',xnew,f2(xnew),'--')
plt.legend(['data','linear','cubic'],loc='best')
plt.show()
import numpy as np
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import *
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)
y = np.exp(-x**2)+0.1 * np.random.randn(50)
'''
print(x,y)

plt.plot(x,y,'ro',ms=5)
plt.show()
'''
'''f1 = interp1d(x,y,kind='linear')
f2 = interp1d(x,y,kind='cubic')
'''
sp1 = UnivariateSpline(x,y)
xnew = np.linspace(-3,3,1000)
sp2 = UnivariateSpline(x,y,k=3,s=0.03)

sp3 = UnivariateSpline(x,y,k=3,s=0.5)

plt.plot(x,y,'ro',xnew,sp1(xnew),'b',xnew,sp2(xnew),'g',xnew,sp3(xnew),'r',lw=3)
#plt.plot(x,y,'ro',xs,sp1(xs),'b',xs,sp2(xs),'g',xs,sp3(xs),'r',xs,f1(xs),'y',lw=3)

plt.show()

print(help(sp1))
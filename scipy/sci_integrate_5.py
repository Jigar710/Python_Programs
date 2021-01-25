from scipy.special import jn
from numpy import *
import matplotlib.pyplot as plt

x = linspace(0,10,100)

fig,ax = plt.subplots()
for n in range(4):
	ax.plot(x,jn(n,x),label=r"$j_%d(x)$" % n)
	
ax.legend()
plt.plot()
plt.show()
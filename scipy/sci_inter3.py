import numpy as np
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import *
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)
y = np.exp(-x**2)+0.1 * np.random.randn(50)

print(x,y)

plt.plot(x,y,'ro',ms=5)
plt.show()

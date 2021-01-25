import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import gridspec

fig = plt.figure(figsize=(8, 6)) 

x = np.linspace(0,10);
y1 = np.sin(x);
plt.subplot2grid((3,3),(0,0),colspan=3)
plt.plot(x,y1)
plt.title('Subplot 1: sin(x)')


y2 = np.sin(2*x);
plt.subplot2grid((3,3),(1,0),colspan=2)
plt.plot(x,y2)
plt.title('Subplot 2: sin(2x)')

y3 = np.sin(3*x);
plt.subplot2grid((3,3),(1,2),rowspan=2)
plt.plot(x,y3)
plt.title('Subplot 3: sin(4x)')

y4 = np.sin(4*x);
plt.subplot2grid((3,3),(2,0))
plt.plot(x,y4)

plt.title('Subplot 4: sin(8x)')

y5 = np.sin(5*x);
plt.subplot2grid((3,3),(2,1))
plt.plot(x,y5)
plt.title('Subplot 5: sin(8x)')

plt.tight_layout()
plt.show()
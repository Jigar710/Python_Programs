import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import gridspec

# plot it
fig = plt.figure(figsize=(8, 6)) 

plt.subplot(2,2,1)
x = np.linspace(0,10);
y1 = np.sin(x);
plt.plot(x,y1)
plt.title('Subplot 1: sin(x)')

plt.subplot(2,2,2)
y2 = np.sin(2*x);
plt.plot(x,y2)
plt.title('Subplot 2: sin(2x)')

#plt.subplot(2,2,3)
y3 = np.sin(4*x);
#plt.plot(x,y3)
plt.title('Subplot 3: sin(4x)')

plt.subplot(2,2,4)
y4 = np.sin(8*x);
plt.plot(x,y4)
plt.title('Subplot 4: sin(8x)')

plt.tight_layout()
plt.show()
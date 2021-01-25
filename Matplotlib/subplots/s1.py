from matplotlib import pyplot as plt
import numpy as np

plt.subplot(2,1,1);
x = np.linspace(0,10);
y1 = np.sin(x);
plt.plot(x,y1)


plt.subplot(2,1,2); 
y2 = np.sin(5*x);
plt.plot(x,y2)

plt.show()
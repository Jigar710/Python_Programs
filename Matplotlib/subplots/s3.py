from matplotlib import pyplot as plt
import numpy as np

plt.subplot(2,2,1);
x = np.linspace(-3.8,3.8);
y_cos = np.cos(x);
plt.plot(x,y_cos);
plt.title('Subplot 1: Cosine')

plt.subplot(2,2,2);
y_poly = 1 - x**2./2 + x**4./24;
plt.plot(x,y_poly,'g');
plt.title('Subplot 2: Polynomial')
'''
plt.subplot(2,2,[3,4]);
plt.plot(x,y_cos,'b',x,y_poly,'g');
plt.title('Subplot 3 and 4: Both')
'''
plt.show()
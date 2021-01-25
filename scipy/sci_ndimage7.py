from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np

f = misc.face()
r = ndimage.gaussian_filter(f,sigma=5)

plt.imshow(r)
plt.show()
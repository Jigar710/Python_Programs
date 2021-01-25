#rotate image
from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np

f = misc.face()
r = ndimage.rotate(f,45)


plt.imshow(r)
plt.show()
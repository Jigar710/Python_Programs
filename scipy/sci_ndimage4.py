#flip image upside down
from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np

f = misc.face()
flip_ud = np.flipud(f)

plt.imshow(flip_ud)
plt.show()
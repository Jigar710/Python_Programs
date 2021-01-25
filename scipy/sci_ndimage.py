from scipy import misc,ndimage
import matplotlib.pyplot as plt

f = misc.face()
plt.imsave('data/face.png',f)

plt.imshow(f)
plt.show()
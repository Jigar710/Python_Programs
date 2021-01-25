from scipy import misc
import matplotlib.pyplot as plt

face = misc.face()

print(type(face))
lx,ly,lz = face.shape

print(lx,ly,lz)
#cropping
crop_face = face[int(lx/4):-int(lx/4),int(ly/4):-int(ly/4)]
plt.imshow(crop_face)
plt.show()
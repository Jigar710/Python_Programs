import matplotlib.pyplot as plt
from scipy import misc

face = misc.face(gray=False)

print(face)
print(type(face))
print(face.shape)
print(face.min(),face.max(),face.mean())
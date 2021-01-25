import numpy as np
import scipy.io as sio

#load the file
mat_file_content = sio.whosmat('array.mat')
print(mat_file_content)
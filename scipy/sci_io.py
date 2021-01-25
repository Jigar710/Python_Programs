import numpy as np
import scipy.io as sio

#save a mat file
vect = np.arange(10)
sio.savemat('array.mat',{'vect':vect})

#load the file
mat_file_content = sio.loadmat('array.mat')
print(mat_file_content)
print(mat_file_content['vect'])

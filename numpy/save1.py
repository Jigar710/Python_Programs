import numpy as np

ar = np.arange(1,10).reshape(3,3)
print(ar)

np.save('arr_data',ar)

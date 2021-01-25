import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.DataFrame(np.random.rand(10,4).cumsum(0),
	columns=['A','B','C','D'],index=np.arange(0,100,10))
#df.plot(subplots=True)
#df.plot(subplots=True,sharex=False)
df.plot(figsize=(10,10))
plt.show()
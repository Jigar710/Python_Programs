import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

data = pd.Series(np.random.rand(10).cumsum(),index=np.arange(1,100,10))
print(data)

data.plot()

plt.savefig('my1.png',bbox_inches='tight')
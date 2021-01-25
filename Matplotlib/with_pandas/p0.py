import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

s = pd.Series(np.random.rand(10).cumsum(),
		index=np.arange(1,100,10))
		
s.plot()
plt.show()
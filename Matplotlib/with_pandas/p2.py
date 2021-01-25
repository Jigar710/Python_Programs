'''
with dataframe bar plots group the values in each row
together in a group in bars, side by side, for each value'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(6,4),
index = ['one','two','three','four','fifth','sixth'],
columns = pd.Index(['A','B','C','D'],name='Genus'))

print(df)

df.plot.bar()
plt.show()
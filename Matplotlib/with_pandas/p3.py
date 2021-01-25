'''
	we create stacked bar plot from a DataFrame
	by passing stacked=True,resulting in the value in each
	row being stacked together.
	A useful receipt for bar plot is to visulize a Series's value
	frequency using value_counts:
		s.value_counts().plot.bar()
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(6,4),
index = ['one','two','three','four','fifth','sixth'],
columns = pd.Index(['A','B','C','D'],name='Genus'))

print(df)

df.plot.barh(stacked=True)
plt.show()
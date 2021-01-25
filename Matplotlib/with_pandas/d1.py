'''
	density : use to plot distribution of data
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

tips = pd.read_csv("examples/tips.csv")
print(tips)

tips['tip'].plot.density()
plt.show()
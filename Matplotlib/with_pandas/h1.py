'''
suppose we wanted to make a stacked bar plot
showing the percentage of data points for each 
party size on each day.
'''
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

tips = pd.read_csv("examples/tips.csv")
print(tips)

#tips['tip'].plot.hist(bins=50)
tips['size'].plot.hist(bins=50)

plt.show()

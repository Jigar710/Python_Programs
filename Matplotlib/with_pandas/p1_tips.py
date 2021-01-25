from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

tips = pd.read_csv("examples/tips.csv")
print(tips)

#tips.plot.bar(subplots=True)
#tips['tip'].plot.bar()
tips['tip'].plot.hist()

plt.show()

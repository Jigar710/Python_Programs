from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

tips = pd.read_csv("examples/tips.csv")
print(tips)

party_counts = pd.crosstab(tips['day'],tips['size'])
print(party_counts)

party_counts = party_counts.loc[:,2:5]
print(party_counts)

party_pct = party_counts.div(party_counts.sum(1),axis=0)
print(party_pct)

party_pct.plot.bar()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("apple2.csv")
print(df.head())

#range(1,10)
rng = pd.date_range(start='4/20/2020',end='5/19/2020',freq='B')
print(rng)

df.set_index(rng,inplace=True)
print(df)

df.Close.plot()
plt.show()
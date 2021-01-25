import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("apple1.csv",parse_dates=['Date'],index_col=0)
print(df.head())

print(df.Close.resample('W').mean())


#df.Close.resample('W').mean().plot()
df.Close.resample('W').mean().plot(kind='bar')
#df.Close.plot()
plt.show()
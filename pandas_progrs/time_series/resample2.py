import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\Coding\Python\13.pandas_progrs\time_series\apple1.csv",parse_dates=['Date'],index_col=0)
if len(df["close"]) > 30:
    period = 30
elif len(df) > 20:
    period = 20
else:
    period = 10
print(len(df))


print(period)
#print(df)
# df.Close.resample('W').mean().plot()
# df.Close.plot()
#plt.show()
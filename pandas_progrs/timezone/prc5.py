import pandas as pd

#df = pd.read_csv("fb.csv")
df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col=0)
print(df)

'''
df = df.shift(-1)
print(df)
'''
'''
df['prv day'] = df['Price'].shift(1)
print(df)
'''
df['1 day diff'] = df['Price'] - df['Price'].shift(1)
print(df)

df['4 day % rtn'] = (df['Price'] - df['Price'].shift(4)) * 100/ df['Price']
print(df)
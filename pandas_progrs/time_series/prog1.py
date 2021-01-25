import pandas as pd

'''
df = pd.read_csv("apple1.csv")
print(df.head())
print(type(df.Date[0]))
'''
'''
df = pd.read_csv("apple1.csv",parse_dates=['Date'])
print(df.head())
print(type(df.Date[0]))
'''

df = pd.read_csv("apple1.csv",parse_dates=['Date'],index_col='Date')
print(df.head())
print(df.index)
import pandas as pd

df = pd.read_csv('data.csv',parse_dates=['day'])
#df.set_index('day',inplace=True)
#df = df.interpolate()	
df = df.interpolate(method='index')	
print(df)
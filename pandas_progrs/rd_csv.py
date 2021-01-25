import pandas as pd

ddf = pd.read_csv("data.csv")
#print(df)
#print(df['day'])
#print(df['event'])
#print(df.loc[0])
#print(df.iloc[0])
'''
print(df['temp'].max())
print(df['temp'].min())
print(df['temp'].mean())
print(df['temp'].describe())

print(df.describe())
'''

#print(df[df['temp'] == df['temp'].max()])
#print(df[df['temp'] > df['temp'].mean()])

#print(df['day'][df['temp'] > df['temp'].mean()])
#print(df[['day','event']][df['temp'] > df['temp'].mean()])

#print(df.head())
#print(df.head(2))
#print(df.columns)
#print(df.index)
'''
print(df)
df.set_index('day',inplace=True)
#new_df = df.set_index('day')
print(df.loc['1/1/2017'])
print(df.iloc[0])

#new_df = df.reset_index()
df.reset_index(inplace=True)'''
print(df)
print(df['day'])
print(df.day)
print(df.day[0])
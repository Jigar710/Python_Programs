import pandas as pd

y = pd.Period('2016-03',freq='M')
print(y)
print(y.start_time)
print(y.end_time)

y = pd.Period('2016-03-31')
print(y)
print(y.start_time)
print(y.end_time)
print(y+1)
'''
y = pd.Period('2016-03-11 10:00:00')
print(y)
print(y.start_time)
print(y.end_time)
'''


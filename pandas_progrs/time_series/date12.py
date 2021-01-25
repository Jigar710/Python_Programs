import pandas as pd

data = '1590395789'

d1 = pd.to_datetime(data,unit='s')
print(d1)

d2 = d1.view('int64')
print(d2)
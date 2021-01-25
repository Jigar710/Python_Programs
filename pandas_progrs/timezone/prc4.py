import pandas as pd
import numpy as np

rng = pd.date_range(start='2017-08-15 09:00:00',periods=10,freq='30min')
print(rng)

s = pd.Series(range(10),index=rng)
print(s)

a = s.tz_localize(tz='US/Eastern')
print(a)

#b = s.tz_localize(tz='Asia/Calcutta')
b = s.tz_localize(tz='US/Eastern')
print(b)

print(a+b)
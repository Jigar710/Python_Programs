import pandas as pd

#rng = pd.date_range(start='1/1/2017',periods=10,freq='H')
#rng = pd.date_range(start='1/1/2017',periods=10,freq='H',tz='Europe/Berlin')
rng = pd.date_range(start='1/1/2017',periods=10,freq='H',tz='dateutil/Europe/Berlin')
print(rng)
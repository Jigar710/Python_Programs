import pandas as pd
#rng = pd.date_range(start='1/1/2017',end='1/31/2017')
#rng = pd.date_range(start='1/1/2017',periods=27,freq='B')
rng = pd.date_range(start='1/1/2017',end='1/31/2017',freq='B')
print(rng)
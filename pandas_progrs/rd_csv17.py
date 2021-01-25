import pandas as pd
import numpy as np

df = pd.read_csv("weather_data.csv")
print(df)
'''
#new_df = df.replace([-99999],np.NaN)
new_df = df.replace([-99999,-88888],np.NaN)

new_df = df.replace({'tempearature':-99999,
'winspeed':-88888,
'event':'no event'},np.NaN)
print(new_df)
'''
new_df = df.replace({
	-99999:0,
	'no event':'Sunny'
	})
print(new_df)

import pandas as pd
import numpy as np
df = pd.read_csv("weather_data.csv")
new_df = df.replace('[a-zA-Z]','',regex=True)
print(new_df)

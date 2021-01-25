import pandas as pd
import numpy as np

#df = pd.DataFrame(np.random.randn(8, 4),index=range(10,81,10), columns=['A', 'B', 'C', 'D'])
df = pd.DataFrame(np.arange(1,33).reshape(8,4),index=range(10,81,10), columns=['A', 'B', 'C', 'D'])
print(df)

#print(df[10])   #error
#print(df[0])    #error
print(df.loc[10])   #1st row  
print(df.iloc[0])   #1st row
print(df['A'])        #1st col
#print(df['A'][0])    #error
print(df['A'][10])     #element

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),index=range(10,81,10), columns=['A', 'B', 'C', 'D'])
print(df)

#df[['A','B']] = df[['B','A']]	#in the same way we can add more columns 
#print(df)

#try this
print(df.loc[:,['A','B','C']])
print(df.loc[:,['A','B','C']])
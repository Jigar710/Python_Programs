import pandas as pd
import numpy as np

#df = pd.DataFrame(np.random.randn(8, 4),index=range(10,81,10), columns=['A', 'B', 'C', 'D'])
df = pd.DataFrame(np.arange(1,33).reshape(8,4),index=range(10,81,10), columns=['A', 'B', 'C', 'D'])
print(df)

print("=============================================")
print(df['A'][10])	#element
#print(df['A':'C'])	#slicing not allowed on str type
#print(df[['A','B']][10])	#error
print("=============================================")
print(df[['A','B'][1]])		#B col
print(df[['A','B']['B']])		#error
print(df[['A','B']]['B'])	#B col
print("=============================================")

print(df['A'][[10,20,30]])	#10, 20, 30 elements
#print(df[['A','B']][[10,20,30]])    #error
print("=============================================")
print(df.loc[10]['A'])	#compare with line number 8 output   #1
print(df.loc[[10,20]]['A'])	#2 element
print("=============================================")
print(df.loc[[10,20]][['A','B']])   #df
print("=============================================")
print(df.loc[10:40])  
print("=============================================")
print(df.loc[10:40]['A'])
print(df.loc[10:40][['A','B']])
print(df.loc[10:40]['A':'D'])

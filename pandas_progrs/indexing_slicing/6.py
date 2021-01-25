import pandas as pd
import numpy as np

dfa = pd.DataFrame(np.random.randn(8, 4),index=range(10,81,10), columns=['A', 'B', 'C', 'D'])
print(dfa)

sa = pd.Series([1,2,3],index=list('abc'))
print(sa)

#attribute access
print(sa.a) #a must exists
#print(sa.d) #try this
print(sa['a']) #a must exists
#print(sa['d']) #try this

#can update data also using labelled indexing
print("==========After updation============")
#sa.a = 100
sa['a'] = 100

#sa.d = 900		#try this
sa['d'] = 1000	# try this
print(sa)

'''
print("==========DataFrame element============")
print(dfa.A)
#print(dfa.Z)#try this
print(dfa['A'])
#print(dfa['Z'])	#try this

print("==========After updation============")
#dfa.A = list(range(len(dfa.index)))
#dfa.Z = list(range(len(dfa.index)))	#try this
dfa['A'] = list(range(len(dfa.index)))
dfa['Z'] = list(range(len(dfa.index)))	#try this
print(dfa)
'''
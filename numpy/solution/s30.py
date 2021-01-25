'''
Write a NumPy program to sort pairs of first name and last name return their
indices. (first by last name, then by first name).
first_names = (Betsey, Shelley, Lanell, Genesis, Margery)
last_names = (Battle, Brien, Plotner, Stahl, Woolum)
Expected Output:
[1 3 2 4 0]
'''
import numpy as np
first_names =    ('Margery', 'Betsey', 'Shelley', 'Lanell', 'AAGenesis')
last_names = ('Woolum', 'ABattle', 'Plotner', 'Brien', 'Stahl')
#x = np.lexsort((first_names, last_names))
x = np.lexsort((last_names,first_names))
print(x)
for i in x:
	print(first_names[i]+" : "+last_names[i])
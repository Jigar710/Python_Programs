from scipy.integrate import quad
from numpy import exp

f = lambda x:exp(-x**2)
i = quad(f,0,1)

print("value : ",i)

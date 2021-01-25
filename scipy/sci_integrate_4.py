import scipy.integrate 
from numpy import exp
from numpy import sqrt

f = lambda x,y : 16*x*y

g = lambda x : 0
h = lambda y : sqrt(1-4*y**2)
i = scipy.integrate.dblquad(f,0,0.5,g,h)

print(i)
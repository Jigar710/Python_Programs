from scipy.integrate import quad
from numpy import *

f = lambda x:exp(-x**2)
val,error = quad(f,-Inf,Inf)

print("value : ",val,error)

analytical = sqrt(pi)
print("Analytically :",analytical)

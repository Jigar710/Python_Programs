from scipy.integrate import quad
from scipy.special import jn
from numpy import *
import matplotlib.pyplot as plt

def integrand(x,n):
	return jn(n,x)
	
x_lower = 0
x_upper = 10	

val,error = quad(integrand,x_lower,x_upper,args=(3,))
print(val,error)
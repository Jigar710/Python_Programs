from scipy import stats
from numpy import *
import matplotlib.pyplot as plt

#create a discrete random variables
#with possion distribution

X = stats.poisson(3.5)

n = arange(0,15)
fix,axes = plt.subplots(3,1,sharex=True)

#plot probability mass function (PMF)
#PMF : value lies between 0 and 1 and sum of area under this function is 1
axes[0].step(n,X.pmf(n))

#plot Cummulitive distribution function (CDF)
#CDF : cummulitive version of PMF
axes[1].step(n,X.cdf(n))

#plot histogram of 1000 random instantiations 
#of the stochastic variable X
axes[2].hist(X.rvs(size=1000))

print(X.mean(),X.std(),X.var())
plt.show()
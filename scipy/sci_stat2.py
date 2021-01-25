from scipy import stats
from numpy import *
import matplotlib.pyplot as plt

#create a discrete random variables
#with normal distribution

Y = stats.norm()
#Y = stats.norm(1,3)
#when will not provide args mean of distribution is 0 and std is 1

n = linspace(-5,5,100)
fix,axes = plt.subplots(3,1,sharex=True)

#plot probability distribution function (PDF)
axes[0].step(n,Y.pdf(n))

#plot Cummulitive distribution function (CDF)
axes[1].step(n,Y.cdf(n))

#plot histogram of 1000 random instantiations 
#of the stochastic variable X
axes[2].hist(Y.rvs(size=1000),bins=50)

print(Y.mean(),Y.std(),Y.var())
plt.show()
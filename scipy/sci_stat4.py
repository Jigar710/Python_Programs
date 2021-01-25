from scipy import stats

Y = stats.norm()

data = Y.rvs(size=1000)
t_statistic,p_value = stats.ttest_1samp(data,0.1)
print("t_statistic :",t_statistic)
print("p_value :",p_value)

t_statistic,p_value = stats.ttest_1samp(data,Y.mean())
print("t_statistic :",t_statistic)
print("p_value :",p_value)
print(Y.mean())

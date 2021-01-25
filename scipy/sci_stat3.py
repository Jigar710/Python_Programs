from scipy import stats

X = stats.poisson(3.5)

t_statistic,p_value = stats.ttest_ind(X.rvs(size=1000),X.rvs(size=1000))
print("t_statistic :",t_statistic)
print("p_value :",p_value)

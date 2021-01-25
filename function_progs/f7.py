#function with keyword args
def cal_salary(name,sal,per=0.80):
	sal = per * sal
	print(name,sal)
	
cal_salary('aaa',1000)
cal_salary('bbb',2000)
cal_salary('ccc',3000)
cal_salary('ddd',5000,0.90)
cal_salary(sal = 5000,name='zzz')
cal_salary(sal = 5000,name='zzz',per=1)
cal_salary(sal = 5000,per=1,name='cde')

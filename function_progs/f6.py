#function with keyword args
def salary(name,sal):
	sal = sal - 0.20 * sal
	print(name,sal)
	
salary('aaa',1000)
salary('bbb',2000)
salary('ccc',3000)
salary('ddd',4000)
salary('eee',5000)

salary(sal=7000,name='fff')
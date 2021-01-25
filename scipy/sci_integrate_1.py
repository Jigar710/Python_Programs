from scipy.integrate import quad

def f(x):
	return x
	
x_lower = 0
x_upper = 1

val,error = quad(f,x_lower,x_upper)

print("value : ",val)
print("Error : ",error)
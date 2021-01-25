def m1():
	yield 1
	yield 2
	yield 3
	yield 4

v = m1()
print(type(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
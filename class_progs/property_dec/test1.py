class Test:
	pass
	
t1 = Test()
t2 = Test()

t1.a = 100
t2.a = 200

print(t1.a)
print(t2.a)

Test.a = 1000
print(Test.a)
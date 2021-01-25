class Zero:
	pass
class First(Zero):
	pass
class Sec(First):
	pass
class Third(Zero):
	pass
class Fourth(Third):
	pass
class Fifth(Sec,Fourth):
	pass
	
print("method resolution order...")
print(Fifth.mro())

#5 ==> 2 ==> 1 ==> 4 ==> 3 ==> 0 ==> Object
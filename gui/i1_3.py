class First:
	pass
class Sec(First):
	pass
class Third:
	pass
class Fourth(Third):
	pass
class Fifth(Sec,Fourth):
	pass
	
print("method resolution order...")
print(Fifth.mro())
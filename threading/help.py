import threading

print(help(threading.Thread()))

forcing positional args
def method(a,b,/):
	pass
forcing keyword args
def method(*,a,b):
	pass
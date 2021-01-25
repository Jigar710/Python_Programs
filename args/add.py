#wap for add of two numbers passed from cmd line args

#python add.py 10 20
import sys

try:
	if(len(sys.argv) == 3):
		print(int(sys.argv[1]) + int(sys.argv[2]))
	elif(len(sys.argv)<3):
		print("insufficient args")
	else:
		print("too much args")
except:
	print("enter numeric data for addition")
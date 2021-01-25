from sys import argv

temp_int = []
temp_str = []
for i in argv[1:]:
	try:
		temp_int.append(int(i))
	except:
		temp_str.append(i)
		
if len(temp_int) > 0:
	print("max of int values :",max(temp_int))
	print("min of int values :",min(temp_int))
if len(temp_str) > 0:
	print("max of str values :",max(temp_str))
	print("min of str values :",min(temp_str))
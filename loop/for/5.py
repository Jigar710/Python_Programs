#wap to disp even number from given limit

a=int(input("enter number"))
b=int(input("enter second values"))
'''
if(a>b):
	a,b = b,a
'''

if(a<b):
	for i in range(a,b+1):
		if(i%2==0):
			print(i,end=" ")
		
else:
	for i in range(a,b-1,-1):
		if(i%2==0):
			print(i,end=" ")
'''
***********...40
hi
$$$$$...30
hello
++++...20
welcome
----...10
bye
........50
'''
def line(n,a):
	for i in range(1,n+1):
		print(a,end="")
		
line(40,'*')
print("\nhi")

line(30,'$')	
print("\nhello")

line(20,'+')	
print("\nbye")

line(10,'-')	
print("\nwelcome")

line(50,'.')	
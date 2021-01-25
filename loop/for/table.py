# wap to create a table of a given number
'''
Enter number 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
...
...
5 * 10 = 50
'''

n = int(input("Enter number : "))

for i in range(1,11):
	print(n," * ",i," = ",n*i)
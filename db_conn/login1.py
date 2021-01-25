import mysql.connector as db

try:
	con = db.connect(host="localhost",user="root",password="",database="python_db")
	cur = con.cursor()
	
	u = input("Enter user name : ")
	p = input("Enter password : ")
	
	q = "select * from users where name = %s and pass = %s"
	
	cur.execute(q,(u,p))
	
	lst = cur.fetchone()
	
	if(lst == None):
		print("id and password does not match")
	else:
		print("welcome")
	#print(lst)
except db.errors.ProgrammingError as e:
	print(e)
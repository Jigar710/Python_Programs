import mysql.connector as db

try:
	con = db.connect(host="localhost",user="root",password="",database="python_db")
	cur = con.cursor()
	
	q = "create table users (id int,name varchar(30),pass varchar(30))"
	#print(q)
#	cur.execute(q)
	q1 = "show tables"
	cur.execute(q1)
	
	lst = cur.fetchall()
	print(lst)
	
except db.errors.ProgrammingError as e:
	print(e)
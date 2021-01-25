import mysql.connector as db

try:
	con = db.connect(host="localhost",user="root",password="",database="python_db")
	cur = con.cursor()
	q = "select * from users"
	
	cur.execute(q)
	lst = cur.fetchall()
	
	print(lst)
except db.errors.ProgrammingError as e:
	print(e)
import mysql.connector as db

try:
	con = db.connect(host="localhost",user="root",password="",database="python_db")
	cur = con.cursor()

	n = input("Enter username : ")
	p = input("Enter password : ")
	
	q = "update users set pass = '"+p+"' where name='"+n+"'"

	cur.execute(q)
	con.commit()
	
except db.errors.ProgrammingError as e:
	print(e)
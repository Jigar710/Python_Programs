import mysql.connector as db

con = db.connect(host="localhost",user="root",password="")
cur = con.cursor()

try:
	db_name = "python_db2"
	q = "create database "+db_name

	cur.execute(q)

	q1 = "use "+db_name
	cur.execute(q1)
	print("database created...")
	
except db.errors.ProgrammingError:
	print("database does not exists")
except db.errors.DatabaseError:
	print("database already exists")
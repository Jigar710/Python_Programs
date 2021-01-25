import mysql.connector as db

try:
	con = db.connect(host="localhost",user="root",password="",database="python_db")
	cur = con.cursor()
	
	q = "update users set pass = 'xyz1' where name='abcd'"

	cur.execute(q)
	con.commit()
	
except db.errors.ProgrammingError as e:
	print(e)
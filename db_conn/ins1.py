import mysql.connector as db

try:
	con = db.connect(host="localhost",user="root",password="",database="python_db")
	cur = con.cursor()
	#q = "insert into users values (1,'kundan','surat')"
	q = "insert into users (name,id,pass) values ('kundan1',2,'surat1')"
	cur.execute(q)
	con.commit()
	print(cur.rowcount)
except db.errors.ProgrammingError as e:
	print(e)
	
'''
insert into users values (1,'kundan','surat')
insert into users (id,name,pass) values (1,'kundan','surat')
insert into users (name,id,pass) values ('kundan',1,'surat')
insert into users (name,id) values ('kundan',1)
'''
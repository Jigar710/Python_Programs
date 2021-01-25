import mysql.connector as db

try:
	con = db.connect(host="localhost",user="root",password="",database="python_db")
	cur = con.cursor()
	
	data = [(10,'kundan1','surat1'),
			(100,'kundan2','surat2'),
			(1000,'kundan3','surat3')]
	
	q = "insert into users values (%s,%s,%s)"
	cur.executemany(q,data)
	con.commit()
	print(cur.rowcount)
except db.errors.ProgrammingError as e:
	print(e)
	
'''
insert into users 
(10,'kundan1','surat1'),
(100,'kundan2','surat2'),
(1000,'kundan3','surat3');
'''
#list all databases

import mysql.connector as db

con = db.connect(host="localhost",user="root",password="")

cur = con.cursor()

db_name = "python_db1"
try:
	q = "create database "+db_name
	cur.execute(q)

	q = "show databases"
	cur.execute(q)

	lst = cur.fetchall()
	#print(lst)
	flag = False
	for i in lst:
		for j in i:
			if j==db_name:
				print("data base created...")
				flag = True
				break
	if(flag==False):
		print("some prob")
except db.errors.DatabaseError:
	print("data base already exists")
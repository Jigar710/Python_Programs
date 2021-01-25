import csv

with open('data2.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	
	row = next(csv_reader)
	print(row)
	print(row['LanguagesWorkedWith'])
	print(row['LanguagesWorkedWith'].split(';'))
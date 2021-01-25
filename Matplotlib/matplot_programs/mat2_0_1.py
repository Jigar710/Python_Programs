import csv
from collections import Counter

with open('data2.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	
	language_counter = Counter()
	
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))

print(language_counter)
print("=======================================")
print(language_counter.most_common(15))
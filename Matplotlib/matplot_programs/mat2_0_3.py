import csv
from collections import Counter
from matplotlib import pyplot as plt

with open('data2.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	
	language_counter = Counter()
	
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))

		
languages = []
popularity = []
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
	
plt.bar(languages,popularity)

plt.legend()

plt.title("Most Popular languges")
plt.xlabel("Programming languages")
plt.ylabel("Number of people who used")

plt.tight_layout()

plt.show()
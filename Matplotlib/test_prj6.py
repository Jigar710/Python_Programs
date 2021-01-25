from collections import Counter
import csv
from matplotlib import pyplot as plt

with open("data2.csv") as csv_file:
	csv_reader = csv.DictReader(csv_file)
	
	langauges_counter = Counter()
	
	for row in csv_reader:
		langauges_counter.update(row['LanguagesWorkedWith'].split(';'))
		
print(langauges_counter)

languages = []
pouplarity = []
for a,b in langauges_counter.most_common(15):
	languages.append(a)
	pouplarity.append(b)
	
print(languages)
print(pouplarity)

languages.reverse()
pouplarity.reverse()

plt.barh(languages,pouplarity)
plt.legend()

plt.title("Most Popular languges")
plt.ylabel("Programming languages")
plt.xlabel("Number of people who used")

plt.tight_layout()

plt.show()
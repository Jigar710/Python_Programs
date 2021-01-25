import csv
from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('data2.csv')
ids = df['Responder_id']	
lang_responses = df['LanguagesWorkedWith']	
	
language_counter = Counter()

for responses in lang_responses:
	language_counter.update(responses.split(';'))
		
languages = []
popularity = []
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
	
languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)


plt.title("Most Popular languges")
plt.xlabel("Number of people who used")
plt.ylabel("Programming languages")

plt.tight_layout()

plt.show()
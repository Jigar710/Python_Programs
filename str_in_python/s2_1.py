'''
input 			: welCoMe tO SuRat
Uppercase		: WELCOME TO SURAT
Lowercase		: welcome to surat
Titlecase		: Welcome To Surat
sen case		: Welcome to surat
Toggle case		: WELcOmE To sUrAT
'''

data = 'welCoMe tO SuRat'
print(data)
#upper case
data_u = ''
for i in data:
	if i>='a' && i<='z':
		data_u = i - 32
		
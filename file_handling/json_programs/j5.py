import json
book = {}
book['title'] = 'Light Science and Magic: An Introduction to Photographic Lighting, Kindle Edition'
book['tags'] = ('Photography', 'Kindle', 'Light')
book['published'] = True
book['comment_link'] = None
book['id'] = 1024

with open(r'E:\Coding\Python\6.file_handling\json_programs\ebook.json',  'w') as f:
	#json.dump(book, f)
	json.dump(book, f,indent=1)
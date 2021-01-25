import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()	

for y in myroot:
	for x in y:
		print(x.tag,x.attrib,x.text)

'''
for x in myroot:
	print(x.tag,x.attrib,x.text)
'''
'''
for x in myroot[0]:
	print(x.tag,x.attrib,x.text)
'''
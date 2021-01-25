import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()	

for x in myroot.findall('food'):
	val1 = x.find('item').text
	val2 = x.find('price').text
	print(val1,val2)
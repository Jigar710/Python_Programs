import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()	

print(myroot.iter())

for x in myroot.iter():
	print(x.tag,x.attrib,x.text)
import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()	

for description in myroot.iter('description'):
	
 new_desc = str(description.text)+'wil be served'
 description.text = str(new_desc)
 description.set('updated', 'yes')
 
mytree.write('new.xml')					

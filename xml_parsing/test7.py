import xml.etree.ElementTree as ET
mytree = ET.parse('sample.xml')
myroot = mytree.getroot()	

ET.SubElement(myroot[0], 'speciality')
for x in myroot.iter('speciality'):
     new_desc = 'South Indian Special'
     x.text = str(new_desc)
 
mytree.write('output5.xml')					
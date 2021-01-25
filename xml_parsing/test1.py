import xml.etree.ElementTree as ET

mytree = ET.parse('sample.xml')
#print(type(mytree))

myroot = mytree.getroot()	

print(myroot)
print(myroot.tag)
'''
print(myroot.attrib)
print(myroot[0])
print(myroot[0].tag)
print(myroot[0][0])
print(myroot[0][0].tag)
print(myroot[0][0].attrib)
print(myroot[0][0].text)
'''
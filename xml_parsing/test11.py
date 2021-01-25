from xml.dom import minidom
p1 = minidom.parse("sample.xml");
print(p1)

tagname= p1.getElementsByTagName('item')
print(tagname)
print(tagname[0])
print(tagname[0].attributes['name'].value)
print(tagname[0].firstChild)
print(tagname[0].firstChild.data)


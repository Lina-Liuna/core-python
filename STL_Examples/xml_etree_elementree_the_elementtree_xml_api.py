
import os
import xml.etree.ElementTree
import xml


tree = xml.etree.ElementTree.parse(os.getcwd() + '/country_data.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print(child.tag, child.attrib)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

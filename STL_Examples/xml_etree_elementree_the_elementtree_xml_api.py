
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

# Modifying an XML file
# ElementTree provides simple way to build XML documents and write them to files.
# ElementTree.write method
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

for country in root.findall('country'):
    # using root.findall() to avoid removal during traversal
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write(os.getcwd() + '/country_data.xml')

# Building XML documents
a = xml.etree.ElementTree.Element('a')
b = xml.etree.ElementTree.SubElement(a, 'b')
c = xml.etree.ElementTree.SubElement(a, 'c')
d = xml.etree.ElementTree.SubElement(c, 'd')

xml.etree.ElementTree.dump(a)

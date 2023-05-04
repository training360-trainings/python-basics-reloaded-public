import xml.etree.ElementTree as ET
from os import path

tree = ET.parse('models.xml')
root = tree.getroot()

# kilistázzuk az összes gyermek elemet a fájlban az attributumokkal együtt
for child in root:
    print(child.tag, child.attrib)

import re
import xml.etree.ElementTree as ET
import logging
from lxml import etree

def parse():
    with open("data/coll/612.xml", encoding="utf8") as file:
        xml_object = ET.fromstring(str(file.read()))
        print(xml_object)


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import lxml
    myParser = lxml.etree.XMLParser(resolve_entities=False, recover=True)
    xmlFile = lxml.etree.parse("data/coll/612.xml", parser=myParser)
    print(xmlFile)
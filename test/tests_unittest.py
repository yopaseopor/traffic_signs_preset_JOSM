import unittest
from lxml import etree

class TestXML(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_xsd(self):
        f_preset = open('Presets_Traffic_signs-preset.xml')
        f_xsd = open('test/tagging-preset.xsd')
        xmlschema_doc = etree.parse(f_xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        doc = etree.parse(f_preset)
        xmlschema.assertValid(doc)

if __name__ == '__main__':
    unittest.main()

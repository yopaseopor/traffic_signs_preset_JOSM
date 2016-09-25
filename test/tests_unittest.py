import unittest
from lxml import etree
import os
import zipfile


class TestXML(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_xsd(self):
        zips = os.listdir('./')
        for zip in zips:
            if os.path.isfile(zip) and zip[-4:] == '.zip':
                print zip
                country = zip.split('.')[0]
                zip_ref = zipfile.ZipFile(zip, 'r')

                pres_name = 'Presets_Traffic_signs-preset_{0}.xml'.format(country)
                data = zip_ref.read(pres_name)
                zip_ref.close()

                f_xsd = open('test/tagging-preset.xsd')
                doc = etree.fromstring(data)
                xmlschema_doc = etree.parse(f_xsd)
                xmlschema = etree.XMLSchema(xmlschema_doc)
                xmlschema.assertValid(doc)

if __name__ == '__main__':
    unittest.main()

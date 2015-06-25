__author__ = 'lacks'

import unittest

from mock import *
from Aechitecture_Lib1 import *
from My_AverageBrightness import *
from xml.etree import ElementTree
import xml

class Toster(unittest.TestCase):

    @patch('urllib.urlopen')
    def test_get_html(self, obj):
        a = Mock()
        a.read.return_value = "kkk"
        obj.return_value = a
        # obj.read.side_effect = "hi"
        self.assertEquals(get_html('ANY'), "kkk")
        self.assertNotEqual(get_html('BLA'), 'aaa')

    def test_shades_of_brightness_funk(self):
        brightness = 167
        shades_of_brightness = [11,11,11,11,11]
        shades_of_brightness_funk(brightness, shades_of_brightness)
        self.assertEquals(shades_of_brightness, [11,11,11,12,11])

    @patch('BeautifulSoup.BeautifulSoup')
    def test_parse(self, obj):
        self.assertEquals(parse(['one', 'two']), [0, 0, 0, 0, 0])

    @patch('urllib.urlopen')
    def test_upload_image(self, obj):
        a = Mock()
        a.read.side_effect = "test_logo"
        obj.return_value = a
        self.assertIsNone(Upload_pictures('.jpg'))
        self.assertIsNone(Upload_pictures('.png'))

    #@patch('xml.etree.ElementTree.parse.getroot')
    #def test_read_xml(self, obj1):
    #    a = Mock()
    #    a.return_value = "adasdsad"
    #    #a.getroot.findall.return_value = []
    #    obj1.return_value = a
    #    read_xml()


if __name__ == '__main__':
    unittest.main()
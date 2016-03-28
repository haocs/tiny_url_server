import unittest
from test import test_support
from urlconverter import UrlConverter as Converter


class UrlConverterTest(unittest.TestCase):
    def test_id_to_url(self):
        self.assertEqual("000001", Converter.id_to_base62_url(1))
        self.assertEqual('00000A', Converter.id_to_base62_url(10))
        self.assertEqual('00000a', Converter.id_to_base62_url(36))
        self.assertEqual('00000z', Converter.id_to_base62_url(61))
        self.assertEqual('00PdmJ', Converter.id_to_base62_url(6111111))

    def test_url_to_id(self):
        self.assertEqual(1, Converter.base62_url_to_id('000001'))
        self.assertEqual(61, Converter.base62_url_to_id("00000z"))
        self.assertEqual(6111111, Converter.base62_url_to_id("00PdmJ"))

def test_main():
    test_support.run_unittest(UrlConverterTest)

if __name__ == '__main__':
    test_main()

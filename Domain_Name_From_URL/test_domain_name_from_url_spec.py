import unittest
from domain_name_from_url import *

class ValidateDomainNameFromURLTestCases(unittest.TestCase):
    """Tests for 'domain_name_from_url.py'"""

    def test_domain_name_from_url(self):
        self.assertEqual(domain_name("http://google.com"), "google")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")

if __name__ == '__main__':
    unittest.main()
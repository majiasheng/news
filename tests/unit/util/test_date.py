import unittest

from news.util import date


class TestDate(unittest.TestCase):
    
    def test_today(self):
        self.assertTrue(date.today())

if __name__ == '__main__':
    unittest.main()

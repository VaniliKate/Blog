import unittest 
from tale import Tale


class TestTale(unittest.TestCase):
    def setUp(self):
    self.new_tale = Tale("38", "Alan Kay", "software today is very much like an Egyptian pyramid", "http://quotes.stormconsultancy.co.uk/quotes/38")
    
    
    def test_init(self):
    self.assertEqual(self.new_tale.id,"38")
    self.assertEqual(self.new_tale.author,"Alan Kay")
    self.assertEqual(self.new_tale.quote, "software today is very much like an Egyptian pyramid")
    self.assertEqual(self.new_tale.url, "http://quotes.stormconsultancy.co.uk/quotes/38")


if __name__ == '__main__':
    unittest.main()



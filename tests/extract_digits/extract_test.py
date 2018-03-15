import unittest

from extract import extract

class ExtractTest(unittest.TestCase):

    def test_unsigned_integer(self):
        number = 12345
        expected_result = ["1", "2", "3", "4", "5"]
        self.assertEqual(extract(number), expected_result)
    
    def test_signed_integer(self):
        number = -10
        expected_result = ["-", "1", "0"]
        self.assertEqual(extract(number), expected_result)
    
    def test_float(self):
        number = 3.14
        expected_result = ["3", ".", "1", "4"]
        self.assertEqual(extract(number), expected_result)

if __name__ == "__main__":
    unittest.main()
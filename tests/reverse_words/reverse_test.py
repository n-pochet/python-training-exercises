import unittest

from reverse import reverse

class ReverseTest(unittest.TestCase):
    
    def test_empty_phrase(self):
        self.assertEqual(reverse(None), "")
    
    def test_simple_phrase(self):
        input_phrase = "This is a test"
        expected_phrase = "test a is This"
        self.assertEqual(reverse(input_phrase), expected_phrase)

    def test_phrase_with_spaces(self):
        input_phrase = "Lot    of spaces   "
        expected_phrase = "spaces of Lot"
        self.assertEqual(reverse(input_phrase), expected_phrase)

if __name__ == '__main__':
    unittest.main()
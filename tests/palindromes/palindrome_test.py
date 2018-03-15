import unittest

from palindrome import is_palindrome

class PalindromeTest(unittest.TestCase):

    def test_simple_palindrome(self):
        input_palindrome = "aba"
        self.assertTrue(is_palindrome(input_palindrome))
    
    def test_empty(self):
        self.assertFalse(is_palindrome(""))
    
    def test_none(self):
        self.assertFalse(is_palindrome(None))
    
    def test_utf8_characters(self):
        input_palindrome = "😆😲😸😲😆"
        self.assertTrue(is_palindrome(input_palindrome))
    
    def test_with_whitespaces(self):
        input_palindrome = "aa  b      aa"
        self.assertTrue(is_palindrome(input_palindrome))

if __name__ == "__main__":
    unittest.main()
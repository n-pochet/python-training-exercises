import unittest

from uniques import uniques

class UniquesTest(unittest.TestCase):

    def test_empty_list(self):
        l = []
        result = uniques(l)
        expected = []
        self.assertEqual(result, expected)
    
    def test_none(self):
        l = None
        result = uniques(l)
        expected = []
        self.assertEqual(result, expected)
    
    def test_simple_list(self):
        l = [1, 3, 2, 5, 1, 3]
        result = uniques(l)
        expected = [1, 2, 3, 5]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
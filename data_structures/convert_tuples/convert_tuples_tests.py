import unittest

from convert_tuples import convert

class ConvertTest(unittest.TestCase):

    def test_none(self):
        l = None
        result = convert(l)
        expected = {}
        self.assertEqual(result, expected)
    
    def test_empty_list(self):
        l = []
        result = convert(l)
        expected = {}
        self.assertEqual(result, expected)
    
    def test_simple_list(self):
        l = [(1, 1), (2, 2)]
        result = convert(l)
        expected = {1: 1, 2: 2}
        self.assertEqual(result, expected)
    
    def test_wrong_tuple(self):
        l = [(1, 1), (1, 2, 'wrong'), (2, 2)]
        result = convert(l)
        expected = {1: 1, 1: 2, 2: 2}
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
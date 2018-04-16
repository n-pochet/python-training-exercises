import unittest

from squares import squares

class SquaresTest(unittest.TestCase):

    def test_zero(self):
        result = squares(0)
        expected = {}
        self.assertEqual(result, expected)
    
    def test_neg_number(self):
        result = squares(-1)
        expected = {}
        self.assertEqual(result, expected)
    
    def test_one(self):
        result = squares(1)
        expected = {1: 1}
        self.assertEqual(result, expected)
    
    def test_three(self):
        result = squares(3)
        expected = {
            1: 1,
            2: 4,
            3: 9
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
import unittest

from key_exists import key_exists

class TestKey(unittest.TestCase):

    def test_empty_dict(self):
        d = {}
        k = 'test'
        result = key_exists(d, k)
        self.assertEqual(result, False)
    
    def test_bad_key(self):
        d = {'1': 1, '2': 2}
        k = 0
        result = key_exists(d, k)
        self.assertEqual(result, False)
    
    def test_correct_key(self):
        d = {'one': 1, 'two': 2}
        k = 'one'
        result = key_exists(d, k)
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()
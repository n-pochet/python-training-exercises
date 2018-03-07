import unittest

from hello import hello

class HelloTest(unittest.TestCase):

    def test_empty_name(self):
        self.assertEqual(hello(), 'Hello, you!')

    def test_simple_name(self):
        self.assertEqual(hello('Jo'), 'Hello, Jo!')

    def test_accented_name(self):
        self.assertEqual(hello('José'), 'Hello, José!')
    
    def test_polish_name(self):
        self.assertEqual(hello('Jarosław'), 'Hello, Jarosław!')

if __name__ == '__main__':
    unittest.main()
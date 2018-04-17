import unittest
import os

from write_file import to_file

class WriteFileTest(unittest.TestCase):

    def test_write_none(self):
        obj = None
        filename = 'none.test'
        to_file(filename, obj)
        with open(filename) as f:
            result = f.read()
        expected = ""
        os.remove(filename)
        self.assertEqual(result, expected)
    
    def test_write_int(self):
        obj = 10
        filename = "int.test"
        to_file(filename, obj)
        with open(filename) as f:
            result = f.read()
        expected = "10"
        os.remove(filename)
        self.assertEqual(result, expected)
    
    def test_write_list(self):
        obj = [1, '2', 3]
        filename = "list.test"
        to_file(filename, obj)
        with open(filename) as f:
            result = f.read()
        expected = "[1, '2', 3]"
        os.remove(filename)
        self.assertEqual(result, expected)
    
    def test_write_dict(self):
        obj = {
            "test": 1,
            "test2": 2
        }
        filename = "dict.test"
        to_file(filename, obj)
        with open(filename) as f:
            result = f.read()
        expected = "{'test': 1, 'test2': 2}"
        os.remove(filename)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
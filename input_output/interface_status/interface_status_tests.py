import unittest
import json

from interface_status import status

HEADER = """Name:     Status:
-----------------\n"""

class IfStatusTest(unittest.TestCase):


    def test_none(self):
        if_status = None
        result = status(if_status)
        expected = HEADER
        self.assertEqual(result, expected)
    
    def test_simple_status(self):
        if_status = [
            {
                "name": "eth1/1",
                "status": "UP"
            }
        ]
        if_status = json.dumps(if_status)
        result = status(if_status)
        expected = HEADER + "eth1/1    UP  \n"
        self.assertEqual(result, expected)
    
    def test_list_status(self):
        if_statuses = [
            {
                "name": "eth1/1",
                "status": "UP"
            },
            {
                "name": "eth1/2",
                "status": "DOWN"
            }
        ]
        if_statuses = json.dumps(if_statuses)
        result = status(if_statuses)
        expected = HEADER + "eth1/1    UP  \neth1/2    DOWN\n"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
import unittest

from line import Line, Point

class LineTest(unittest.TestCase):

    def test_none_point(self):
        p = None
        self.assertRaises(
            TypeError,
            Line,
            p,
            p
        )
    
    def test_same_point_len(self):
        p1 = Point(1, 1)
        p2 = Point(1, 1)
        l = Line(p1, p2)
        result = l.length()
        expected = 0
        self.assertEqual(result, expected)
    
    def test_y_axis_line(self):
        p1 = Point(0, 0)
        p2 = Point(0, 5)
        l = Line(p1, p2)
        result = l.length()
        expected = 5
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
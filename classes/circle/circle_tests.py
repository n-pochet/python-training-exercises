import unittest

from circle import Circle 

class CircleTest(unittest.TestCase):

    def test_zero_radius(self):
        c = Circle(0)
        perimeter = c.perimeter()
        area = c.area()
        exp_perimeter = 0
        exp_area = 0
        self.assertEqual(perimeter, exp_perimeter)
        self.assertEqual(area, exp_area)
    
    def test_negative_radius(self):
        self.assertRaises(
            ValueError,
            Circle,
            -1
        )
    
    def test_positive_radius(self):
        c = Circle(10)
        perimeter = c.perimeter()
        area = c.area()
        exp_perimeter = 62.83185307179586
        exp_area = 314.1592653589793
        self.assertEqual(perimeter, exp_perimeter)
        self.assertEqual(area, exp_area)

if __name__ == "__main__":
    unittest.main()
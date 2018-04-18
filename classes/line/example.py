from math import pow, sqrt

class Point():
    """Point class
    """


    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    """Line class
    
    Raises:
        TypeError -- Raises if p1 or p2 is not an instance of Point
    """


    def __init__(self, p1, p2):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError
        self.p1 = p1
        self.p2 = p2

    def length(self):
        """Length of the line
        
        Returns:
            float -- Length of the line
        """

        x1 = self.p1.x
        x2 = self.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        l = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        return l
import math

PI = math.pi

class Circle():
    """Circle
    
    Raises:
        ValueError -- Raises ValueError if radius is < 0
    """


    def __init__(self, radius):
        if radius < 0:
            raise ValueError
        self.radius = radius
    
    def perimeter(self):
        """Perimeter
        
        Returns:
            float -- Perimeter of the circle
        """

        return 2 * PI * self.radius
    
    def area(self):
        """Area
        
        Returns:
            float -- Area of the circle
        """

        return PI * self.radius * self.radius
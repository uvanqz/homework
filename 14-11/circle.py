import math
class NotValidFigure(Exception):
    pass

class Circle:
    def __init__(self, r):
        self.r = r
        if not self.is_valid():
            raise NotValidFigure
    
    def get_length(self):
        return 2 * math.pi * self.r
    
    def get_ploshad(self):
        return math.pi * (self.r ** 2)

    def is_valid(self):
        radius = [self.r]
        if all([isinstance(ra, (int, float)) for ra in radius]):
            return all([ra > 0 for ra in radius])
circle = Circle(5)
print(circle.get_length())
print(circle.get_ploshad())

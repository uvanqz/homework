import math
class Circle:
    def __init__(self, r):
        self.r = r
    
    def get_length(self):
        return 2 * math.pi * self.r
    
    def get_ploshad(self):
        return math.pi * (self.r ** 2)

circle = Circle(5)
print(circle.get_length())
print(circle.get_ploshad())

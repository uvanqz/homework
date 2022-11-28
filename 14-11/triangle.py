class NotValidFigure(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise NotValidFigure

    def get_perimeter(self):
        return self.a + self.b + self.c
    
    def get_ploshad(self):
        p = self.get_perimeter() / 2
        return (p*(p - self.a) * (p - self.b) * (p - self.c))**0.5

    def is_valid(self):
        sides = [self.a, self.b, self.c]
        if all([isinstance(side, (int, float)) for side in sides]):
            return all([side > 0 and self.get_perimeter() - 2 * side > 0 for side in sides])

triangle = Triangle(5, 3, 7)
print(triangle.get_perimeter())
print(triangle.get_ploshad())  

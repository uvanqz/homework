class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c
    
    def get_ploshad(self):
        p = self.get_perimeter() / 2
        return (p*(p - self.a) * (p - self.b) * (p - self.c))**0.5

triangle = Triangle(15, 13, 17)
print(triangle.get_perimeter())
print(triangle.get_ploshad())

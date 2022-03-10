class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def __str__(self):
        return f'Restangle (Width = {self.width}, Height = {self.height})'

class Circle:
    def __init__(self, r):
        self.radius = r
    def __str__(self):
        return f'Circle (Radius = {self.radius})'

class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
    def __str__(self):
        return f'Triangle (Side a = {self.side_a}, Side b = {self.side_b}, Side c = {self.side_c})'

rectangle = Rectangle(5, 14)
circle = Circle(33)
triangle = Triangle(2, 4, 6)

print(rectangle)
print(circle)
print(triangle)

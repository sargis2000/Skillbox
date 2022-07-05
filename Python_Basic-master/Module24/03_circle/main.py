from math import pi


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.pi = pi
        self.x = x
        self.y = y
        self.radius = r

    def get_area(self):
        return self.radius ** 2 * self.pi

    def get_perimeter(self):
        return 2 * self.radius * self.pi

    def scale(self, k):
        self.radius *= k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.radius + other.r) ** 2


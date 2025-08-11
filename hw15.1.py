class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        new_width = self.width
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.get_square() * n
        new_width = self.width
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f'Rectangle(width={self.width:.2f}, height={self.height:.2f}, area={self.get_square():.2f})'

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

print(r1)
print(r2)

r3 = r1 + r2
print(r3)

r4 = r1 * 4
print(r4)

print(Rectangle(3, 6) == Rectangle(2, 9))

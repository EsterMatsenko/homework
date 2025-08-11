from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути нулем")
        self.a = a
        self.b = b
        self._simplify()

    def _simplify(self):
        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common
        if self.b < 0:
            self.b = -self.b
            self.a = -self.a

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        numerator = self.a * other.b + self.b * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.a * other.b - self.b * other.a
        denominator = self.b * other.b
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}/{self.b}"

# Приклади 
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
print(f"f_b + f_a = {f_c}")

f_d = f_b * f_a
print(f"f_b * f_a = {f_d}")

f_e = f_a - f_b
print(f"f_a - f_b = {f_e}")

print(f"f_d < f_c: {f_d < f_c}")
print(f"f_d > f_e: {f_d > f_e}")
print(f"f_a != f_b: {f_a != f_b}")

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
print(f"f_1 == f_2: {f_1 == f_2}")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}; {self.y})"

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):  # /
        return Vector(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):  # //
        return Vector(self.x // other.x, self.y // other.y)


if __name__ == "__main__":
    v1 = Vector(5, 3)
    v2 = Vector(7, 2)

    print("v1 is", v1)
    print("v2 is", v2)
    print("v1 + v2 =", v1 + v2)
    print("v1 * v2 =", v1 * v2)

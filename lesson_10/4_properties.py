class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    @property
    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    rect = Rectangle(3, 4)
    print(rect.area)  # output: 12

    rect.width = 5
    rect.height = 6
    print(rect.area)  # output: 30

    # rect.width = -1  # raises ValueError: Width must be positive.

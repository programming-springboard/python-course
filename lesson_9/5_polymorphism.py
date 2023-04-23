from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_area(self):
        return self._width * self._height


class Square(Shape):
    def __init__(self, width):
        self._width = width

    def get_area(self):
        return self._width * 2


class ShapeIn3d:
    def __init__(self, shape_in_2d, length):
        self._shape_in_2d = shape_in_2d
        self._length = length

    def get_volume(self):
        area_of_2d_shape = self._shape_in_2d.get_area()
        return area_of_2d_shape * self._length


if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    square = Square(5)

    rectangle_in_3d = ShapeIn3d(rectangle, length=5)
    square_in_3d = ShapeIn3d(square, length=7)

    print(rectangle.get_area(), rectangle_in_3d.get_volume())
    print(square.get_area(), square_in_3d.get_volume())

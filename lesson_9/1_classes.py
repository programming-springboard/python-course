class Rectangle:
    """
    This class represents a rectangle object with a given width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def get_area(self):
        """
        Calculates the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.width * self.height


if __name__ == "__main__":
    rectangle = Rectangle(width=5, height=10)
    print("The area of the rectangle with width=5 and height=10 is ", rectangle.get_area())

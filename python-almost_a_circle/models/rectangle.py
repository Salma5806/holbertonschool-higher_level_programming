#!/usr/bin/python3
"""models Rectangle"""
from .base import Base


class Rectangle(Base):
    """main class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Width Getter
        """
        return self.__width

    @property
    def height(self):
        """
            height Getter
        """
        return self.__height

    @property
    def x(self):
        """
            x Getter
        """
        return self.__x

    @property
    def y(self):
        """
            y Getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Ser x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Area width * height
        """
        return self.width * self.height

    def display(self):
        """display character"""
        for i in range(self.y):
            print()
        for j in range(self.height):
           print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns formatted information display
        """

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates rectangle values
        """

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

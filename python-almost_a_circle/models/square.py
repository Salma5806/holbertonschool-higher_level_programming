#!/usr/bin/python3
"""models Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """size needs to be an int
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <size>
        """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,self.id, self.x, self.y,self.width)



#!/usr/bin/python3
"""models Rectangle classess"""



class Rectangle(Base):
     """class Rectangle with
     Args :
          __width : width of rectangle
          __height : height of rectangle
          __x : number
          __y : number
     """

     def __init__(self, width, height, x=0, y=0, id=None):
         super().__init__(id)
         self.width = width
         self.height = height
         self.x = x
         self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @property
    def y(self):
        """Get y"""
        return self.__y


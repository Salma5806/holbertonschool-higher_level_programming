#!/usr/bin/python3
"""This module creates a Square class that inherts from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class named Rectangle
    Attributes:
    size: size of square
    """
    def __init__(self, size):
       """initialization of square"""
       self.__size = size
       self.integer_validator("size", size)

    def area(self):
       """returns area of instance"""
       return self.__size * self.__size
    def __str__(self):
       return ("[Rectangle] {}/{}".format(self.__size, self.__size))

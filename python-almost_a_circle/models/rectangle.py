#!/usr/bin/python3
"""Module Rectangle"""
from .base import Base


class Rectangle(Base):
    """
    Defines class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

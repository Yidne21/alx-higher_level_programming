#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

"""
A Module which calculates the area of A circle
"""

class Square(Rectangle):
    """
    A class which is The subclass of The rectangle class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
    """
    Calculate The are of the Circle and return the result
    """
        return self.__size * self.__size


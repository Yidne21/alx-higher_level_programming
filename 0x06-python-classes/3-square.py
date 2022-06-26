#!/usr/bin/python3
"""square class with private attribute size and method area"""
class Square:
    """initialization of size by __init__ mmethod and returning the area using the area method"""
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2

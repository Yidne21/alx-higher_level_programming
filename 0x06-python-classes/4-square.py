#!/usr/bin/python3
"""The square class with getter and setter"""
class Square:
    """initilization of __size"""
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        """returning the __size value"""
        return self.__size

    @size.setter
    def size(self, size):
        """setting the size"""
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2

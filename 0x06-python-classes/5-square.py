#!/usr/bin/python3
""" Square class with getter, setter and initilizer method
"""
class Square:
    """initilizes the private attribute __size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        """Returns the value of __size
        """
        return self.__size

    @size.setter
    def size(self, size):

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area

        """
        return self.__size ** 2

    def my_print(self):
        """Prints # until self.area() + 1
        """
        if self.__size == 0:
            print()
            return None

        for i in range(1, self.area() + 1):
            print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()

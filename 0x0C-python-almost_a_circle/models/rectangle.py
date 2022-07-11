#!/usr/bin/python3
"""
Module which contains the Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    A rectangle class which is the subclass of the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initilizes the width, height, x, y and the id instance attribute
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Returns the private attribute width
        """
        return self.__width

    @width.setter
    def width(self, param):
        """
        Sets the private attribute width with the incomming parameter param
        """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """
        Returns the private attribute height to the caller
        """
        return self.__height

    @height.setter
    def height(self, param):
        """
        sets the private attribute height with the incomming parameter param
        """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """
        Returns the private attribute x to the caller
        """
        return self.__x

    @x.setter
    def x(self, param):
        """
        sets the private attribute x with the incomming parameter param
        """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """
        Returns the private attribute y to the caller
        """
        return self.__y

    @y.setter
    def y(self, param):
        """
        Sets the private attribute y with the incomming parameter param
        """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """
        validate the incomming parameter value and param
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangles data
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """
        returns the string representation of the rectangle class 
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update the rectanle private properties using the *args and **kwargs argument accepters
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle class properties
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

#!/usr/bin/python3
"""
A module which contains the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class which is the subclass of the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initilizes the private instance attributes of the Square class with the super class instance attributes
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns the string representation of the Square class 
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        returns the private instance atrribute width to the caller
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        initilizes the private instance attribute width and height with incomming parammeter value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the private instance attribute of the square class using *args and **kwargs argument accepters 
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square class attributes or properties
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

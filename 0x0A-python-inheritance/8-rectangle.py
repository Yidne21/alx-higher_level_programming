#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module which intiate and valididate it's argument by using Integer validator
"""

class Rectangle(BaseGeometry):
      """
      The subclass of the BaseGeometry Class
      """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

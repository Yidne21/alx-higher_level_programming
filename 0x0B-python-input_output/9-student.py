#!/usr/bin/python3
"""Student class module"""


class Student:
    """"Studnet Class wwith to_json method"""

    def __init__(self, first_name, last_name, age):
        """"Initilizes the public instance variable"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of a python class"""

        return self.__dict__

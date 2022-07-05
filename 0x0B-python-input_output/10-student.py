#!/usr/bin/python3
"""Student class module"""


class Student:
    """Student class which has to_json and reload_from_json methods"""

    def __init__(self, first_name, last_name, age):
        """initilizes the public instance variable"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method which returns class_d it the attributr exists on the list otherwise it returns the sel_d"""

        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]

            return sel_d

        return class_d

    def reload_from_json(self, json):
        """reloads the JSON file"""

        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]

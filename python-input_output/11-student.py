#!/usr/bin/python3
"""
    a class Student
"""


class Student:
    """
    a class Student
    """
    def __init__(self, first_name, last_name, age):
        """instatiation of first_name, last_name, age

        Attributes:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance

        Returns:
            dict: A dictionary representation of a Student instance
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

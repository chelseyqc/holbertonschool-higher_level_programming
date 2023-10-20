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

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance

        Returns:
            dict: A dictionary representation of a Student instance
        """
        return self.__dict__

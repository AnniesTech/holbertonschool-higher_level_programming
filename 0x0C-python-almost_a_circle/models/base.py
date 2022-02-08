#!/usr/bin/python3
"""Definition of class Base"""
import json
from logging import exception


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string representation
        of list_dictionaries
        - list_dictionaries is a list of dictionaries
        - If list_dictionaries is None or empty, return the string: "[]"
        - Otherwise, return the JSON
        string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
            return string

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:
        - list_objs is a list of instances who inherits of Base
        - If list_objs is None, save an empty list
        - The filename must be: <Class name>.json - example: Rectangle.json """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                result = [objects.to_dictionary() for objects in list_objs]
                jsonfile.write(Base.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:
        - json_string is a string representing a list of dictionaries
        - If json_string is None or empty, return an empty list
        - Otherwise, return the list represented by json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:
        - **dictionary can be thought of as a
            double pointer to a dictionary
        - To use the update method to assign all attributes,
            you must create a “dummy” instance before:
        - Create a Rectangle or Square instance with
            “dummy” mandatory attributes (width, height, size, etc.)
        - Call update instance method to this “dummy”
            instance to apply your real values"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances:
        - The filename must be: <Class name>.json - example: Rectangle.json
        - If the file doesn’t exist, return an empty list"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except Exception:
            return []

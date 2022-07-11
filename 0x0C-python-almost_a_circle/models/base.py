#!/usr/bin/python3
"""Defines Base class"""


import json
import os
import csv
import turtle
import random


class Base():
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """"Writes the JSON string representation of list_objs to a file"""
        save = "[]"
        if (list_objs is not None and type(list_objs) == list
                and list_objs != []):
            save = cls.to_json_string([
                instance.to_dictionary() for instance in list_objs])
        with open(cls.__name__ + ".json", "w") as f:
            f.write(save)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if (json_string == '' or json_string is None
                or type(json_string) != str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        ins_list = []
        if os.path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", "r") as f:
                list_ouput_of_dicts = cls.from_json_string(f.read())
            for dict in list_ouput_of_dicts:
                ins_list.append(cls.create(**dict))
        return ins_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        save = "[]"
        if cls.__name__ == "Rectangle":
            header = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            header = ["id", "size", "x", "y"]
        if (list_objs is not None and type(list_objs) == list
                and list_objs != []):
            save = [instance.to_dictionary() for instance in list_objs]
        with open(cls.__name__ + ".csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=header)
            w.writerows(save)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        list_inst = []
        if os.path.exists(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv", "r") as f:
                if cls.__name__ == "Rectangle":
                    header = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    header = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=header)
                list_dict = [dict((k, int(v)) for k, v in row.items())
                             for row in reader]
            list_inst = [cls.create(**dict) for dict in list_dict]
        return list_inst

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        a = turtle.Turtle()
        turtle.bgcolor("cyan")
        a.pensize(3)
        a.shape("turtle")
        for rect in list_rectangles:
            a.color("black", "white")
            a.begin_fill()
            for i in range(2):
                a.forward(rect.width)
                a.left(90)
                a.forward(rect.height)
                a.left(90)
            a.penup()
            a.goto(rect.width, rect.height)
            a.pendown()
            a.end_fill()

        a.left(140)
        a.penup()
        a.forward(100)
        a.pendown()
        a.right(140)
        a.left(90)
        a.shape("circle")
        a.pensize(3)
        a.begin_fill()
        for sqa in list_squares:
            a.color("white", "green")
            for i in range(2):
                a.forward(sqa.size)
                a.left(90)
                a.forward(sqa.size)
                a.left(90)
            a.left(90)
            a.penup()
            a.goto(1, -10*i)
            a.pendown()
        a.end_fill()
        turtle.done()

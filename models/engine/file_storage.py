#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):

                   """sets in __objects the obj with key <obj class name>.id"""

                           key = "{}.{}".format(type(obj).__name__, obj.id)

                                   FileStorage.__objects[key] = obj



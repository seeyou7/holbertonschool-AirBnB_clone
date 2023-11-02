#!/usr/bin/python3

import json
from os import path


class FileStorage:
    """ class to serialize instance to json and deserialize
        json file to instance
    """
    
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ """

    def save(self):
        """ """

    def reload(self):

#!/usr/bin/python3
"""Filestorage class"""

import models
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
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file
            (path: __file_path)
        """
        serialized_objects = {}

        for key, obj in FileStorage.__objects.items():

            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as file:
                    json_data = json.load(file)
                    for key, obj_data in json_data.items():
                        class_name, obj_id = key.split('.')
                        cls = globals()[class_name]
                        obj = cls(**obj_data)
                        FileStorage.__objects[key] = obj
        except Exception as e:
            print("Error during reload: {}".format(str(e)))

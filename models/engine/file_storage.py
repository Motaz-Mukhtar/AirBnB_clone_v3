#!/usr/bin/python3
""" the storage engine """
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ returns the dictionary __objects if it's None
            else returns the list of objects of one type class
        """
        if cls is None:
            return (self.__objects)
        else:
            my_dict = {}
            if type(cls) == str:
                cls = eval(cls)
            for key, value in self.__objects.items():
                if type(value) == cls:
                    my_dict[key] = value
            return my_dict

    def new(self, instance):
        """ add in __objects the obj with key <obj class name>.id """
        if instance:
            key = "{}.{}".format(instance.__class__.__name__, instance.id)
            self.__objects[key] = instance

    def save(self):
        """ Save the Instances at file.json """
        s_dict = {i: self.__objects[i].to_dict()
                  for i in self.__objects.keys()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(s_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised) """
        # excutes only if file exists
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete the obj from __objects if it's insied
            if obj is equal to None, the method should
            not do anything
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """ Call reload() method for deseriaizing the JSON file """
        self.reload()

#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd
import json3
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import models
from models.base_model import BaseModel
from models.user import User

class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        }

class HBNBCommand(cmd.Cmd):
    """using python command line Cmd"""
    prompt = "(hbnb) "

    def do_create(self, line):
        """create Model"""
        if not line:
            print("** class name missing **")
            return
        try:
            create_instance = class_mapping.get(line)()
            create_instance.save()
            print(create_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """show Model id"""
        if not line:
            print("** class name missing **")
            return
        arg = line.split()
        if arg[0] not in class_mapping:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg[0], arg[1])
        loaded_objects = models.storage.all()
        loaded_instance = loaded_objects.get(key)
        if not loaded_instance:
            print("** no instance found **")
            return
        print(loaded_instance)

    def do_destroy(self, line):
        """destroy Model id"""
        arg = line.split()
        if not arg:
            print("** class name missing **")
            return
        if arg[0] not in class_mapping:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg[0], arg[1])
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]
        models.storage.save()

    def do_all(self, line):
        """all Model"""
        objs = models.storage.all()
        if line and line not in class_mapping:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objs.values() if not line or obj.__class__.__name__ == line])

    def do_count(self, line):
        """all Model"""
        objs = models.storage.all()
        if line and line not in class_mapping:
            print("** class doesn't exist **")
            return
        count = len([obj for obj in objs.values() if not line or obj.__class__.__name__ == line])
        print(count)

    def do_update(self, line):
        """update object attributes"""
        comand = line.split()
        ln = len(comand)
        if ln < 2:
            print("** class name missing **")
            return
        if comand[0] not in class_mapping:
            print("** class doesn't exist **")
            return
        if ln < 3:
            print("** instance id missing **")
            return
        if ln < 4:
            print("** attribute name missing **")
            return
        if ln < 5:
            print("** value missing **")
            return
        key = "{}.{}".format(comand[0], comand[1])
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        instance = objs[key]
        try:
            value = int(comand[3])
        except ValueError:
            try:
                value = float(comand[3])
            except ValueError:
                value = comand[3]
        setattr(instance, comand[2], value)
        models.storage.save()

    def default(self, line):
        """default command"""
        try:
            parts = line.split('.')
            if len(parts) != 2:
                raise ValueError
            class_name, rest = parts
            action, rest = rest.split('(', 1)
            if not action or not rest.endswith(')'):
                raise ValueError
            params = rest[:-1].split(',')
            if not params:
                raise ValueError
            if action == 'all' and len(params) == 0:
                self.do_all(class_name)
            elif action == 'count' and len(params) == 0:
                self.do_count(class_name)
            elif action == 'show' and len(params) == 1:
                self.do_show(f"{class_name} {params[0].strip()}")
            elif action == 'destroy' and len(params) == 1:
                self.do_destroy(f"{class_name} {params[0].strip()}")
            elif action == 'update' and len(params) >= 2:
                arg_str = f"{class_name} {params[0].strip()}"
                for pair in params[1:]:
                    key, value = pair.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    arg_str += f" {key} {value}"
                self.do_update(arg_str)
            else:
                raise ValueError
        except ValueError:
            pass

    def do_EOF(self, line):
        """Quit program if EOF entered"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit console"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


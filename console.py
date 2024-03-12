#!/usr/bin/python3
"""Quit command to exit the program"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Quit command to exit the program"""
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj_key = args[0] + '.' + args[1]
            obj = storage.all().get(obj_key)
            if not obj:
                print("** no instance found **")
                return
            print(obj)
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj_key = args[0] + '.' + args[1]
            obj = storage.all().get(obj_key)
            if not obj:
                print("** no instance found **")
                return
            del storage.all()[obj_key]
            storage.save()
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        try:
            objects_list = [str(obj) for obj in objects.values()
                            if type(obj).__name__ == args[0]]
            print(objects_list)
        except Exception:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            obj_key = args[0] + '.' + args[1]
            obj = storage.all().get(obj_key)
            if not obj:
                print("** no instance found **")
                return
            setattr(obj, args[2], args[3])
            obj.save()
        except Exception:
            print("** class doesn't exist **")

    def default(self, arg):
        """task advanced"""
        switch = 0
        try:
            list = arg.split('(')
            print(list)
            if ')' in list:
                list.remove(')')
                switch = 1
            mainfs = list[0].split('.')
            funk = mainfs[1]
            objec = mainfs[0]
            if len(list) == 1:
                if funk == "all":
                    self.do_all(objec)
                if funk == "count":
                    self.do_count(objec)
            else:
                scndfs = list[1].split(',', 1)
                if switch == 0:
                    id4 = scndfs[0][0:-1].strip('"')
                elif switch == 1:
                    id4 = scndfs[0].strip('"')
                if funk == "show":
                    self.do_show("{} {}".format(objec, id4))
                if funk == "destroy":
                    self.do_destroy("{} {}".format(objec, id4))
        except Exception:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

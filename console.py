#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
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
        except Exception as e:
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
        except Exception as e:
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
        except Exception as e:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        try:
            objects_list = [str(obj) for obj in objects.values() if type(obj).__name__ == args[0]]
            print(objects_list)
        except Exception as e:
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
        except Exception as e:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()


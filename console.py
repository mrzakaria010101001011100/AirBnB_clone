#!/usr/bin/env python3
"""This module defines the HBNBCommand class, a command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Print help message for the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl-D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Inventory(cmd.Cmd):
    prompt = 'inventory> '

    def __init__(self):
        super().__init__()
        self.items = {}

    def do_create(self, line):
        """Create a new item. Usage: create <name> <description>"""
        args = line.split()
        if len(args) < 2:
            print("Usage: create <name> <description>")
            return
        name = args[0]
        description = ' '.join(args[1:])
        self.items[name] = Item(name, description)
        print(f"Item {name} created.")

    def do_show(self, name):
        """Show the details of an item. Usage: show <name>"""
        if name not in self.items:
            print("Item not found.")
            return
        item = self.items[name]
        print(f"Name: {item.name}")
        print(f"Description: {item.description}")

    def do_delete(self, name):
        """Delete an item. Usage: delete <name>"""
        if name not in self.items:
            print("Item not found.")
            return
        del self.items[name]
        print(f"Item {name} deleted.")

    def do_list(self, line):
        """List all items."""
        for name, item in self.items.items():
            print(f"Name: {item.name}, Description: {item.description}")

    def do_quit(self, line):
        """Quit the program."""
        return True

if __name__ == '__main__':
    Inventory().cmdloop()


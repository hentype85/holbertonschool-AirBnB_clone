#!/usr/bin/python3
"""AirBnB console"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class console"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program ctrl-d"""
        print()
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, args):
        """ Create a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if len(args) == 0:
            print("** class name missing **")
        try:
            new = eval(args)()
            new.save()
            print(new.id)
        except Exception:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

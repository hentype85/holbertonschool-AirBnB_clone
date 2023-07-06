#!/usr/bin/python3
"""AirBnB console"""

import cmd


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
        """ empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

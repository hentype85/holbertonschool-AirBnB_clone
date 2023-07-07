#!/usr/bin/python3
"""AirBnB console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class console"""

    prompt = "(hbnb) "
    all_classes = {
        "BaseModel": BaseModel,
        }

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

    def do_show(self, args):
        """ Prints the string representation of an
            instance based on the class name and id"""
        if len(args) == 0:
            print("** class name missing **")
        else:
            list_args_splitted = args.split(" ")
            if list_args_splitted[0] not in self.all_classes:
                print("** class doesn't exist **")
            if len(list_args_splitted) < 2:
                print("** instance id missing **")
            else:
                class_name = list_args_splitted[0]
                class_id = list_args_splitted[1]
                key = "{}.{}".format(class_name, class_id)
                try:
                    print(storage.all()[key])
                except Exception:
                    print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)"""
        if len(args) == 0:
            print("** class name missing **")
        else:
            list_args_splitted = args.split(" ")
            if list_args_splitted[0] not in self.all_classes:
                print("** class doesn't exist **")
            if len(list_args_splitted) < 2:
                print("** instance id missing **")
            else:
                try:
                    class_name = list_args_splitted[0]
                    class_id = list_args_splitted[1]
                    key = "{}.{}".format(class_name, class_id)
                    del storage.all()[key]
                    storage.save()
                except Exception:
                    print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

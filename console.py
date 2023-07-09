#!/usr/bin/python3
"""AirBnB console"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class console"""

    prompt = "(hbnb) "
    all_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
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
            list_args = args.split(" ")
            if list_args[0] not in self.all_classes:
                print("** class doesn't exist **")
            if len(list_args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(list_args[0], list_args[1])
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
            list_args = args.split(" ")
            if list_args[0] not in self.all_classes:
                print("** class doesn't exist **")
            if len(list_args) < 2:
                print("** instance id missing **")
            else:
                try:
                    key = "{}.{}".format(list_args[0], list_args[1])
                    del storage.all()[key]
                    storage.save()
                except Exception:
                    print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances
            based or not on the class name"""
        list_args = args.split()
        dict_objs = storage.all()
        new_list = []
        if len(list_args) > 0:
            if list_args[0] not in self.all_classes:
                print("** class doesn't exist **")
            else:
                for k, v in dict_objs.items():
                    if list_args[0] == v.__class__.__name__:
                        new_list.append(str(v))
        else:
            for k, v in dict_objs.items():
                new_list.append(str(v))
        if len(new_list) != 0:
            print(new_list)

    def do_update(self, args):
        """Updates an instance and save JSON file)"""
        list_args = args.split()

        if len(list_args) == 0:
            print("** class name missing **")
        elif list_args[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(list_args) == 1:
            print("** instance id missing **")
        elif len(list_args) == 2:
            print("** attribute name missing **")
        elif len(list_args) == 3:
            print("** value missing **")
        else:
            key = list_args[0] + "." + list_args[1]
            instance = storage.all()[key]

            if key in storage.all():
                attr_name = list_args[2]
                attr_value = list_args[3].strip('"')

                if attr_name in instance.__dict__:
                    setattr(instance, attr_name, attr_value)
                    instance.save()
                else:
                    new_dict = {attr_name: attr_value}
                    new_dict.update(instance.__dict__)
                    instance.__dict__.clear()
                    instance.__dict__.update(new_dict)
                    instance.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

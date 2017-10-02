#!/usr/bin/python3
"""Command Interpreter - Console"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand - console for the AirBnB clone
        Note: "help <cmd>" functionality is provided by cmd module
    """

    # ----- basic Holberton AirBnB commands -----
    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Prevents previous command from executing again
        """
        pass

    # ----- basic Console CRUD commands -----
    def do_create(self, arg):
        """Create BaseModel instance, saves to JSON file, prints ID"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print('{}'.format(obj.id))

    def do_show(self, arg):
        """Show object"""
        input = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if input[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(input) == 1:
                print("** instance id missing **")
            else:
                allObjs = storage.all()
                if input[1] in allObjs.keys():
                    for input[1] in allObjs.keys():
                        print(allObjs[input[1]])
                else:
                    print("** no instance found **")

    # def do_destroy(self, arg):
    # something

    def do_all(self, arg):
        """Show all objects"""
        isPrint = False
        if len(arg) == 1 and arg[0] == "all":
            isPrint = True
        elif len(arg) == 2 and arg[0] == "all" and arg[2] == "BaseModel":
            isPrint = True
        else:
            print("** class doesn't exist **")
        if isPrint:
            allObjs = storage.all()
            if input[1] in allObjs.keys():
                for input[1] in allObjs.keys():
                    print(allObjs[input[1]])
            else:
                print("** no instance found **")

    # def do_update(self, arg):
    # something

if __name__ == '__main__':

    intro = '** Welcome to the AirBnB clone. Type help or ? to list commands **'
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop(intro)

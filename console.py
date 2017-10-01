#!/usr/bin/python3
"""Command Interpreter - Console"""
import cmd
from models.base_model import BaseModel


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

    # ----- basic CRUD commands -----
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
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[1] != "BaseModel":
            print("** class doesn't exist **")
        elif arg[2] == None:
            print("** instance id missing **")
        # else:
            # objAll = BaseModel.all()
            # if arg[2] in objAll: #Must iterate and find matching ID
            # If instance of the class name doesn't exist for the id
            # print("** no instance found **") (ex: $ show BaseModel 121212)
        else:
            # prints the string of instance of class name and id.
            # Ex: $ show BaseModel 1234-1234-1234
            pass # temp statement

    # def do_destroy(self, arg):
    # def do_all(self):
    # def do_update(self, arg):

if __name__ == '__main__':

    intro = '** Welcome to the AirBnB clone. Type help or ? to list commands **'
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop(intro)

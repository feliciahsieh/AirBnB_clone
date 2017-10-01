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
        """Create BaseModel instance"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            bm = BaseModel()
            bm.save()
            print('{}'.format(bm.id))

    def do_show(self):
        """Show object"""

    # def do_destroy(self):
    # def do_all(self):
    # def do_update(self):

if __name__ == '__main__':

    intro = '** Welcome to the AirBnB clone. Type help or ? to list commands **'
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop(intro)

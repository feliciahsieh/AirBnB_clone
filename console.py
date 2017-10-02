#!/usr/bin/python3
"""Command Interpreter - Console"""

import cmd
import models
# from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand - console for the AirBnB clone
        Note: "help <cmd>" functionality is provided by cmd module
    Usage:
        create [class=BaseModel]
        show [class=BaseModel [id=12234-1234-1234]]
        destroy [class=BaseModel] [id=1234-1234-1234]
        all | all [class=BaseModel]
        update [class=BaseModel] [id=1234-1234-1234] [key] [value]
    """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "
        self.intro =  "******************************************************\n"
        self.intro += "* Welcome to the AirBnB clone. Type help for cmds    *\n"
        self.intro += "******************************************************\n"

    # ----- basic AirBnB clone commands -----
    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Do nothing on empty input line
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
        """Show class object with ID"""
        input = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if input[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(input) == 1:
                print("** instance id missing **")
            else:
                allObjs = models.storage.all()
                print(allObjs)
                # if input[1] in allObjs.keys():
                #    for input[1] in allObjs.keys():
                #        print(allObjs[input[1]])
                # else:
                #    print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an object"""
        input = arg.split()
        allObjs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif input[0] != "BaseModel":
            print(input[0])
            print("** class doesn't exist **")
        elif len(input) == 1:
            print("** instance id missing **")
        elif input[1] in allObjs.keys():
            print("Destroy:", input[1])
            del allObjs[input[1]] # missing logic
            allObjs.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Show all objects"""
        input = arg.split()
        allObjs = models.storage.all()
        if len(arg) == 0:
            print(models.storage.all())
        elif (len(input) == 1 and input[0] == "BaseModel"):
            for k in allObjs:
                if input[0] in k:
                    print(allObjs[k])  # missing logic
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update obj atribute with info
        """
        input = arg.split()
        if len(input) == 0:
            print("** class name missing **")
        elif input[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(input) == 1:
            print("** instance id missing **")
        elif input[2] not in { "1234-1234-1234" }: # missing logic
            print("** no instance found **")
        elif len(input) == 2:
            print("** attribute name missing **")
        elif input[2] not in allObjs.keys(): # missing logic
            print("** value missing **")
        elif len(input) > 4:
            # don't execute
            pass
        else:
            # allObjs = models.storage.all()
            # allObjs.save()
            pass

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()

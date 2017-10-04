#!/usr/bin/python3
"""Command Interpreter - Console"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        self.intro = "****************************************************\n"
        self.intro += "* Welcome to the AirBnB clone. Type help for cmds  *\n"
        self.intro += "****************************************************\n"
        self.types = {'BaseModel': BaseModel, 'User': User, 'State': State,
                      'City': City, 'Amenity': Amenity, 'Place': Place,
                      'Review': Review}
        self.__count = models.storage.count()

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
            return
        if arg in self.types:
            obj = self.types[arg]()
            obj.save()
            print(obj.id)
            self.__count[obj.__class__.__name__] += 1
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show class object with ID"""
        input = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(input) == 1:
            print("** instance id missing **")
            return
        if input[0] in self.types:
            allObjs = models.storage.all()
            realID = input[0] + "." + input[1]
            if realID in allObjs:
                print(allObjs[realID])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy an object"""
        input = arg.split()
        if len(input) == 2:
            realID = input[0] + "." + input[1]
        allObjs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(input) == 1:
            print("** instance id missing **")
            return
        if input[0] in self.types:
            if realID in allObjs:
                allObjs.pop(realID)
                self.__count[input[0]] -= 1
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print(input[0], "** class doesn't exist **")

    def do_all(self, arg):
        """Show all objects"""
        input = arg.split()
        allObjs = models.storage.all()
        if len(arg) == 0:
            for k in allObjs:
                print(allObjs[k])
        elif (len(input) == 1 and input[0] in self.types):
            for k in allObjs:
                if input[0] in k:
                    print(allObjs[k])
        else:
            print("** class doesn't exist **")

    def do_update(self, args, **kwargs):
        """Update obj atribute with info
        """
        if args:
            args = args.split()
            argsize = len(args)
            if argsize >= 2:
                ID = args[0] + "." + args[1]
            else:
                if argsize == 1:
                    print("** instance id missing **")
                elif argsize == 0:
                    print("** class name missing **")
                return
        try:
            d = models.storage.all()[ID].to_dict()
            if kwargs:
                d.update(kwargs)
            else:
                for i in range(0, argsize, 2):
                    if i >= 2:
                        args[i] = args[i].strip(':')
                        args[i] = args[i].strip('"')
                        args[i+1] = args[i+1].strip('"')
                        d[args[i]] = args[i+1]
            d.pop("updated_at")
            d.pop("__class__")
            self.types[args[0]](**d)
        except:
            print("** no instance found **")
        


    def default(self, line):
        """default behavior method"""
        import re
        import ast
        js = {}
        methods = {'all': self.do_all, 'show': self.do_show,
                   'destroy': self.do_destroy, 'update': self.do_update}
        ln = re.split('[.,()]', line)
        if '{' in line:
            js = ast.literal_eval(re.search('({.+})', line).group(0))
            ln = ln[:3]
        meth = ln.pop(1)
        if meth == "show" or meth == "update":
            ln[1] = ln[1].strip('"')
        elif meth == "count":
            print(self.__count[ln[0]])
            return
        ln = " ".join(ln)
        ln = ln.replace('\'','"') 
        if meth in methods:
            methods[meth](ln, **js)

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()

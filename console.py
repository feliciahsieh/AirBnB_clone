#!/usr/bin/python3
"""Command Interpreter - Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    def do_quit(self, args):
        """Quit command to exit the program."""
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program."""
        raise SystemExit

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop('')

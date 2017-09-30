#!/usr/bin/python3
"""Command Interpreter - Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand - console for the AirBnB clone
    """

    def do_quit(self, args):
        """
        do_quit - Quit command to exit the program
        Args:
            args(tuple) - arguments sent with the quit command
        Return:
            None
        """
        raise SystemExit

    def do_EOF(self, args):
        """
        do_EOF - EOF command to exit the program
        Args:
            None
        Return:
            None
        """
        raise SystemExit

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop('')

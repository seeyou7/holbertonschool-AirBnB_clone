#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
""" entry point of command interpreter """


class HBNBCommand(cmd.Cmd):
    """ class for the console """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ exit the l.cmd using cntrl D """
        print()
        return True

    def emptyline(self):
        """ Do nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3

import cmd
""" entry point of command interpreter """


class HBNBCommand(cmd.Cmd):
    """ class for the console """

    prompt = '(hbnb)'

    def quit(self, arg):
        """ to exit the cmd line interpreter """
        return True

    def EOF(self, arg):
        """ exit the l.cmd using cntrl D """
        print()
        return True

    def emptyline(self):
        """ Do nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

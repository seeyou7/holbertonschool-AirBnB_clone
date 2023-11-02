#!/usr/bin/python3

import cmd
""" entry point of command interpreter """


class HBNBCommand(cmd.Cmd):
    """ class for the console """

    prompt = '(hbnb)'

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ exit the l.cmd using cntrl D """
        print()
        return True

    def emptyline(self):
        """ Do nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

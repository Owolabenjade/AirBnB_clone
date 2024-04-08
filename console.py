#!/usr/bin/python3
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_help(self, arg):
        'Help command. Lists available commands.'
        super().do_help(arg)

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


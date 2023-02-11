#!/usr/bin/python3
import cmd

class MyShell(cmd.Cmd):
    intro = 'Welcome to my shell. Type help or ? to list commands.\n'
    prompt = '(myshell) '
    file = None

    # Define commands
    def do_greet(self, args):
        """Greet the user"""
        print("Hello World!")

    def do_exit(self, args):
        """Exits from the shell"""
        return True

if __name__ == '__main__':
    MyShell().cmdloop()

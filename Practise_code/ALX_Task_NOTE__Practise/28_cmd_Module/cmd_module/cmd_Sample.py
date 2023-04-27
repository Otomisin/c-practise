import cmd

class MyCmdInterpreter(cmd.Cmd):
    prompt = 'MyCmd> '
    intro = 'Welcome to MyCmd! Type ? to list commands'

    def do_hello(self, arg):
        """Say hello to the user"""
        print(f"Hello, {arg}!")

    def do_quit(self, arg):
        """Quit the command interpreter"""
        print('Goodbye!')
        return True

if __name__ == '__main__':
    MyCmdInterpreter().cmdloop()

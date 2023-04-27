class Parent1:
    def say_hello(self):
        print("Hello from Parent1!")

class Parent2:
    def say_hello(self):
        print("Hello from Parent2!")

class Child(Parent1, Parent2):
    def say_hello(self):
        # Call the say_hello method from Parent1 using super()
        super(Parent1, self).say_hello()
        # Call the say_hello method from Parent2 using super()
        super(Parent2, self).say_hello()

# Create an instance of Child and call its say_hello method
c = Child()
c.say_hello()

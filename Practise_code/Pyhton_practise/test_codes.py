class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
Fruits = Fruit("Apple", "red")

# Modifying Object Properties
Fruits.name = "strawberry"

# calling the instance method using the object obj
Fruits.show()
# Output Fruit is strawberry and Color is red
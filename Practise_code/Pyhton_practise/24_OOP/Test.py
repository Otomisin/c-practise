# # !/usr/bin/python3

"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size

my_square = Square(3)

print(type(my_square))

# print(my_square.__dict__)

print(my_square.__size)
# print(my_square.size)

try:
    print(my_square.size)
except Exception as e:
    print(e)
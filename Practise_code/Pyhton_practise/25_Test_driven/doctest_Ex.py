def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaaa'
    """
    return a * b

# # To Acess the docstring in terminal 
# python example.py -v
# use python3 -m doctest -v doctest_Ex.py to test your file

# # Check if the docstring
# help(my_function)
# help(my_function.add)
# print(my_function.__doc__)

# use Doctest to check
if __name__ == "__main__":
    import doctest
    doctest.testmod()

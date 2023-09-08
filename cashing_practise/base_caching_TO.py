#!/usr/bin/python3
""" BaseCaching module
"""
# This line indicates that the script should be run with Python 3. It also serves as a module-level docstring.

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    # This class-level docstring describes the purpose and main attributes of the BaseCaching class.

    MAX_ITEMS = 4
    # This is a class-level constant specifying the maximum number of items the cache can store.

    def __init__(self):
        """ Initialize
        """
        # This is the constructor method for the class. It initializes an instance of the class.
        
        self.cache_data = {}
        # Initializes an empty dictionary to store cache data.

    def print_cache(self):
        """ Print the cache
        """
        # This method prints the current state of the cache.

        print("Current cache:")
        # Print header for the cache output.

        for key in sorted(self.cache_data.keys()):
            # Sorts the keys and iterates through them.
            
            print("{}: {}".format(key, self.cache_data.get(key)))
            # Print each key-value pair in the cache.

    def put(self, key, item):
        """ Add an item in the cache
        """
        # This method is intended to add a new item to the cache.

        raise NotImplementedError("put must be implemented in your cache class")
        # Raises an error because this is a base class and the method is meant to be implemented by derived classes.

    def get(self, key):
        """ Get an item by key
        """
        # This method is intended to retrieve an item from the cache by its key.

        raise NotImplementedError("get must be implemented in your cache class")
        # Raises an error because this is a base class and the method is meant to be implemented by derived classes.

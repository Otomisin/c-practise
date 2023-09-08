#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching_TO import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None


# Create an instance of the BasicCache
my_cache = BasicCache()
my_cache.print_cache()

# Add items to the cache
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "Oluwalogbon")

# Retrieve items from the cache
my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# print(my_cache.get("D"))
# my_cache.print_cache()
# my_cache.put("D", "School")
# my_cache.put("E", "Battery")
# my_cache.put("A", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))

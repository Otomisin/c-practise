from simple_parent_cache import BaseCaching

class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]


# Create an instance of BasicCache
cache = BasicCache()

# Add items to the cache
cache.put("name", "John")
cache.put("age", 30)
cache.put("class", "class 2")
cache.put("sex", "Female")

# Retrieve items from the cache
print('Name:', cache.get("name")) # John
print('Age :', cache.get("age"))   # 30
print('sex:', cache.get("sex"))

# Attempting to retrieve a non-existing item
print('Address:', cache.get("address"))    # class 1 (default value for int type)


# Attempting to retrieve an item with a None key
print(cache.get(None))

import redis

# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
redis_client.set('my_key', 'my_value')

# Retrieve the value for a key
value = redis_client.get('my_key')
print(value.decode('utf-8'))  # Convert bytes to string

# Increment a counter
redis_client.incr('my_counter')

# Get the current value of the counter
counter_value = redis_client.get('my_counter')
print(int(counter_value))

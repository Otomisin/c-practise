"""
MAP, REDUCE AND FILTER

https://tonyj.me/blog/map-reduce-and-filter-python/
https://www.youtube.com/watch?v=kj850Y8y8FI&ab_channel=Telusko

"""

"""
FILTER
Filter takes two arguments, a function and a collection of objects
"""
# Create a list of even numbers using lambda and filter

num_list = list(filter(lambda a: a % 2 == 0, range(10)))
print('This is the even list using lambda', num_list)

"""
MAPS
The map takes a function and a collection as its arguments. 
"""
doub_map = list(map(lambda n: n*2, num_list))
print('This is double using map: ', doub_map)

"""
REDUCE
Reduce takes a function and a collection of objects as arguments and returns a 
value that is created by combining the items in the collection. 
"""
from functools import reduce
print(doub_map)
sumReduc = reduce(lambda a, b: a + b, doub_map)

print(sumReduc)


"""
COMBINING MAP, FILTER AND REDUCE
find the sum of squares of all even numbers from a list of numbers.
"""

from functools import reduce

squares_sum = reduce(lambda acc, num: acc + num,
                map(lambda num: num**2,
                filter(lambda x: x % 2 == 0, range(10))))
print('Output for the combining is: ', squares_sum) # Outputs 120
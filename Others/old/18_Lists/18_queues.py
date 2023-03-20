"""
USING LISTS AS QUEUES
5.1.2. Using Lists as Queues
It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”);
however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or
pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:
"""

from collections import deque
queue = deque(["Eric", "John", "Michael"])
print('The first sets', queue)

queue.append("Terry")           # Terry arrives to the right
queue.append("Graham")          # Graham arrives to the right
print('Add Terry and Graham', queue)  # Add Terry and Graham

queue.popleft()
print('List after a popleft 1 ', queue)  # The first (Eric) to arrive no leaves

queue.popleft()
print('List after a popleft 2 ', queue)  # The first (John) to arrive no leaves


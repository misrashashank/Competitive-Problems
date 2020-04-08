'''
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate
the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


from collections import OrderedDict


class LRUCache:

    '''
    # Method 1: Using dictionary and stack
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_map = {}
        self.lru_stack = []

    def get(self, key: int) -> int:
        if key in self.lru_map.keys():
            self.lru_stack.remove(key)
            self.lru_stack.append(key)
            return self.lru_map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.lru_map) == self.capacity:
            if key in self.lru_map.keys():
                self.lru_stack.remove(key)
                self.lru_stack.append(key)
                self.lru_map[key] = value
            else:
                # Remove least recently used element
                lru_element = self.lru_stack.pop(0)
                del self.lru_map[lru_element]
                self.lru_map[key] = value
                self.lru_stack.append(key)
        else:
            self.lru_map[key] = value
            if key in self.lru_stack:
                self.lru_stack.remove(key)    
            self.lru_stack.append(key)
    '''

    # Method 2: Using in-build OrderedDict
    def __init__(self, capacity: int):
        self.lru_map = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.lru_map.keys():
            return -1
        else:
            self.lru_map.move_to_end(key)
            return self.lru_map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lru_map.keys():
            self.lru_map.move_to_end(key)
        self.lru_map[key] = value
        if len(self.lru_map) > self.capacity:
            self.lru_map.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

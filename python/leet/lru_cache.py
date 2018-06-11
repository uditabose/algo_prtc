
class Entity(object):
    """
    key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return ("%s:%s" % (self.key, self.value))
            
class Node(object):
    """
    doubly linked node/list
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return ("%s > %s" % 
                (self.value, 
                 ('None' if self.next == None else str(self.next))))
        

class LRUCache(object):
    '''
    Design and implement a data structure for 
    Least Recently Used (LRU) cache. It should support 
    the following operations: get and put.

    get(key) - Get the value (will always be positive) 
    of the key if the key exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value 
    if the key is not already present. When the cache 
    reached its capacity, it should invalidate the least 
    recently used item before inserting a new item.

    Follow up:
    Could you do both operations in O(1) time complexity?
    https://leetcode.com/problems/lru-cache/description/

    Time :
    Space:
    Note : @see https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-+-Double-LinkedList
    '''
    
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError(" error")
        self.first = None
        self.last = None
        self.mapped = {}
        self.capacity = capacity

    def put(self, key, value):
        node = Node(Entity(key, value))
        

        if self.capacity > len(self.mapped): # hasn't reached max capacity
            if len(self.mapped) == 0: # starting to create the list
                self.first = self.last = node
            else: # adding node at the end
                node.prev = self.last
                self.last.next = node
                self.last = node

            self.mapped[key] = node
            
        else: # is max, so pop the first elem, and reset
            lru_node = self.first
            if lru_node:
                #print("%d > %d" % (self.first.value.key, -1))
                del self.mapped[lru_node.value.key]
                self.first = lru_node.next
                if self.first:
                    self.first.prev = None
                del lru_node

            # reset the last node
            node.prev = self.last
            self.last.next = node
            self.last = node
            if self.first == None:
                self.first = self.last
            self.mapped[key] = node
            
    def get(self, key):
        if key in self.mapped: # key is being accessed
            mru_node = self.mapped[key] # most recently used node
            
            # reset the list to extract MRU node
            prev = mru_node.prev
            next = mru_node.next
            mru_node.prev = None
            mru_node.next = None
            
            if prev:
                prev.next = next
            else: # extracted node was the first node
                self.first = next
            
            if next:
                next.prev = prev
            else: # extracted node was the last node
                self.last = prev


            # add the MRU node at the end of the list
            if self.last == None:
                self.last = mru_node
            else :
                self.last.next = mru_node
                mru_node.prev = self.last
                self.last = mru_node
            if self.first == None:
                self.first = self.last
            return mru_node.value.value
        else:
            return -1

    def __str__(self):
        return str(self.first) if self.first != None else "nada"
      
def run():
    '''
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    print(cache.get(1))   # returns 1
    print(cache)
    cache.put(3, 3)
    print(cache)           
    print(cache.get(2));  # returns -1 (not found)    
    cache.put(4, 4);      # evicts key 2 // evicts key 1
    print(cache.get(1))   # returns -1 (not found)
    print(cache.get(3))   # returns 3
    print(cache.get(4))   # returns 4
    print(cache)
    '''
    cache = LRUCache(1)
    cache.put(2, 1)
    print(cache)
    print(cache.get(2))
    print(cache)


if __name__ == '__main__':
    run()


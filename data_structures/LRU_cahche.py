#################################################################################
## Category: Doubly Linked List (storing key, value, prev, next pointers)
## Title: Design a data structure that follows the constrains of the Least Recent Used Cache
## Short notes -
##    Need to use doubly linked to track least and most used items in the list
##    need to use dictionary to update the existing key items in doubly linked list
## Youtube Link: https://www.youtube.com/watch?v=7ABFKPK2hD4&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=13&ab_channel=NeetCode
## Input: [put, put, put, put, put, get, lru, mru]
#         [(1,1), (2,2), (3,3), (4,4), (5,5), (2,2), (3,3), (2,2)]
## Output: [null, null, null, null, null(deleted (1,1) due to limit 4), (3,3),  (2,2)]
##################################################################################


#Instanticated node with key, value and prev, next pointers as null
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


## LRUCache will be instanticated and called as such:
## obj = LRUCache(capacity)
## Params = obj.get(key)
## obj.put(key, value)
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} #map key to node

        #left =LRU , right= Most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    #Remove from list
    def remove(self, node: Node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    #insert to right side
    def insert(self, node: Node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  #removing from list
            self.insert(self.cache[key]) #adding right before the right node
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #removing from list
        self.cache[key] = Node(key, value)  #Updating/Adding to cache dictiorany
        self.insert(self.cache[key]) #adding right before the right node
        print(f'INSERTED:: [{key}, {value}]')
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru) #Removing from right after the left node
            del self.cache[lru.key] #Removing from cache dictiorany
            print(f'DELETED DUE TO CAPACITY LIMIT({self.capacity}):: [{lru.key}, {lru.value}]')

    def get_lru(self) -> list: #Get least recent used value
        return [self.left.next.key, self.left.next.value]

    def get_mru(self) -> list: #Get most recent used value
        return [self.right.prev.key, self.right.prev.value]


lrun_cache = LRUCache(4)
lrun_cache.put(1, [1, 1])
lrun_cache.put(2, [2, 2])
lrun_cache.put(3, [3, 3])
lrun_cache.put(4, [4, 4])
lrun_cache.put(5, [5, 5])
lrun_cache.get(2) # most recent used [2, [2,2]]
print(f'LEAST RECENT USED:: {lrun_cache.get_lru()}')
print(f'MOST RECENT USED::  {lrun_cache.get_mru()}')




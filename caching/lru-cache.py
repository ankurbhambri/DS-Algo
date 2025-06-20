# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # map key to node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from last (rear)
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node at head (front)
    def insert(self, node):
        next_node = self.left.next
        self.left.next = next_node.prev = node
        node.prev, node.next = self.left, next_node

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove from the tail (right of linked list) and delete the LRU from hashmap
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
print(obj.get(1))
obj.put(4, 4)
print(obj.get(2))
obj.put(5, 5)
print(obj.get(4))

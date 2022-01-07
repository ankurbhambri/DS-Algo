class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):

        self.cap = capacity
        self.cache = {}  # map key to node
        """ 
        left will point least recently uses and 
        right will point for most recently used 
        """
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        """Removing from left so left is dummy node
        left dummy node wil change its connection with next to it
        and will make connection with node's next one
        Like left temp - > n1 -> n2- n2 -> right dummy
        so in this case left tmp -> n2 -> n3 -> right dummy."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        """Inserting at right most side
        In this case we change temp right connection with new node
        Like left temp - > n1 -> n2- n2 -> right dummy
        left temp - > n1 -> n2- n2 -> n3 -> right dummy
        """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            print(self.cache[key].val)
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the left of linked list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            print(lru in self.cache)
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

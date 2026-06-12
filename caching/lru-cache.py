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



'''
    A question very similar to designing LFU cache was asked. The only difference was there were changes in key-value eviction property. 
    Keys were numbers. Values were in the format [ Content : String, Score : INT]. Once we have accessed a key-value pair, the score was supposed to increase by 1. 
    While evicting I need to follow the standard pattern but I was supposed to evict only those values whose score was even.
'''

# Variant: What if we have score with value and we can only eveict even score keys?

class Node:
    def __init__(self, key, content, score):
        self.key = key
        self.content = content
        self.score = score
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Dummy head aur tail taaki boundary conditions handle na karni padein
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def insert(self, node):
        """Node ko list ke end (tail se pehle) mein add karta hai (Most Recently Used)."""
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        self._size += 1

    def remove(self, node):
        """Kisi bhi node ko list se remove karta hai."""
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        self._size -= 1

    def remove_head(self):
        """Sabse purana node (head ke baad wala) remove karta hai (Least Recently Used)."""
        if self._size == 0:
            return None
        oldest_node = self.head.next
        self.remove(oldest_node)
        return oldest_node

    def is_empty(self):
        return self._size == 0


class LFUEvenCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}        # key -> Node
        self.freq_map = {}     # score -> DoublyLinkedList
        self.min_score = float('inf')  # Minimum score present in cache (for eviction)

    def _update_score(self, node):

        """Node ka score 1 se badhata hai aur use nayi score list mein move karta hai."""
        old_score = node.score
        
        # 1. Purani score list se remove karo
        self.freq_map[old_score].remove(node)
        if self.freq_map[old_score].is_empty():
            del self.freq_map[old_score]
            # Agar yahi min_score wali list thi, to min_score ko bump karo
            # (kyunki score sirf +1 hota hai, baaki sab >= old_score + 1)
            if old_score == self.min_score:
                self.min_score = old_score + 1

        # 2. Score badhao
        node.score += 1
        new_score = node.score
        
        # 3. Nayi score list mein daalo
        if new_score not in self.freq_map:
            self.freq_map[new_score] = DoublyLinkedList()
        self.freq_map[new_score].insert(node)

    def get(self, key: int) -> str:
        if key not in self.cache:
            return "Not Found"
        
        node = self.cache[key]
        self._update_score(node)  # Access hone par score +1 hoga
        return node.content

    def put(self, key: int, content: str, initial_score: int):
        if self.capacity <= 0:
            return

        # Case 1: Key pehle se exist karti hai (Sirf update hoga)
        if key in self.cache:
            node = self.cache[key]
            node.content = content
            self._update_score(node)
            return

        # Case 2: Cache full hai, Eviction karna padega
        if len(self.cache) >= self.capacity:
            evicted = self._evict_even_score_node()
            if not evicted:
                print("Eviction failed: No even score found to evict!")
                return # Interviewer ke custom fallback ke hisab se yahan change ho sakta hai

        # Case 3: Naya node insert karo
        new_node = Node(key, content, initial_score)
        self.cache[key] = new_node
        
        if initial_score not in self.freq_map:
            self.freq_map[initial_score] = DoublyLinkedList()
        self.freq_map[initial_score].insert(new_node)

        # min_score update karo agar naya score chhota hai
        if initial_score < self.min_score:
            self.min_score = initial_score

    def _evict_even_score_node(self) -> bool:
        """min_score se shuru karke sabse chhota EVEN score dhoondh kar evict karta hai."""
        if not self.freq_map:
            return False

        # min_score se start; agar wo odd hai to +1 karke nearest even pe jao
        score = self.min_score
        if score % 2 != 0:
            score += 1

        # Sirf existing even scores mein se smallest dhoondho (min_score se aage)
        candidate = None
        for s in self.freq_map.keys():
            if s % 2 == 0 and s >= score:
                if candidate is None or s < candidate:
                    candidate = s

        if candidate is None:
            return False

        dll = self.freq_map[candidate]
        evicted_node = dll.remove_head()
        if not evicted_node:
            return False

        # Cache se bhi delete karo
        del self.cache[evicted_node.key]
        if dll.is_empty():
            del self.freq_map[candidate]

        # Cache empty ho gaya to min_score reset karo;
        # warna agar evicted score == min_score tha to min_score ko
        # remaining freq_map ki smallest key tak badha do
        if not self.cache:
            self.min_score = float('inf')

        elif candidate == self.min_score and candidate not in self.freq_map:
            self.min_score = min(self.freq_map.keys())

        print(f"Evicted Key: {evicted_node.key} (Score: {candidate})")
        return True
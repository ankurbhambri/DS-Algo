import collections


class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        # self.freq = 1
        # self.size = 0

    def __str__(self):
        return "{} {}".format(self.key, self.val)


class DLL:
    def __init__(self):
        self.head = Node("Head", "H")  # Dummy Nodes
        self.tail = Node("Tail", "T")  # Dummy Nodes
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertAtTail(self, key, val):
        temp = Node(key, val)
        tail = self.tail.prev
        tail.next = temp
        temp.prev = tail
        temp.next = self.tail
        self.tail.prev = temp
        self.size += 1
        return temp

    def removeFromHead(self):
        temp = self.head.next
        self.removeNode(temp)

        return temp

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        # del node


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = collections.defaultdict(DLL)
        self.cache = dict()
        self.keyToLmap = dict()
        self.size = 0
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.updateFreq(key, self.cache[key][1])
        return self.cache[key][1]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key not in self.cache:
            if self.size == self.cap:
                """
                1. capacity is now full so we have to remove LFU.
                2. LFU number we have in min_freq so we have to remove from d[min_freq]
                3. First element from d[min_freq] will be removed.
                """
                temp = self.d[self.min_freq].removeFromHead()
                del self.cache[temp.key]
                del self.keyToLmap[temp.key]
            temp = self.d[1].insertAtTail(key, value)
            self.keyToLmap[key] = temp
            self.min_freq = 1
            self.cache[key] = (1, value)
            if self.size < self.cap:
                self.size += 1
        else:
            self.updateFreq(key, value)

    def updateFreq(self, key, value):
        """
        Update Freq works in following way:
            1. Retrieve freq and value of key
            2. From keyToLmap dict get address of linkedlist of key
            3. Remove key value from current freq.
            4. Append key to freq+1 list.
        :param value:
        :param key:
        :return:
        """
        prevFreq, _ = self.cache[key]
        currFreq = prevFreq + 1
        self.d[prevFreq].removeNode(self.keyToLmap[key])
        self.keyToLmap[key] = self.d[currFreq].insertAtTail(key, value)
        if self.d[self.min_freq].size == 0:
            self.min_freq += 1
        self.cache[key] = (currFreq, value)

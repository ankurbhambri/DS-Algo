# https://leetcode.com/problems/lfu-cache/

from collections import defaultdict


class Node:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = prev
        self.next = nxt


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, head_node, new_node):  # head -> here ...... <- tail
        new_node.next = head_node.next
        new_node.prev = head_node
        head_node.next.prev = new_node
        head_node.next = new_node

    # removing where the node is present and changing its prev and next pointers only
    def remove(self, node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Key to Node mapping
        self.freq_map = defaultdict(DLL)
        self.min_freq = 0

    def _update_freq(self, node):

        freq = node.freq
        self.freq_map[freq].remove(node)  # remove node from its prev frequency list

        # check if that freq is empty, if yes remove from cache
        if (
            self.min_freq == freq
            and self.freq_map[freq].head.next == self.freq_map[freq].tail
        ):
            self.min_freq += 1  # increase min_freq
            del self.freq_map[freq]

        node.freq += 1  # give incremented freq to the node

        # insert front of that freq list
        self.freq_map[node.freq].insert(self.freq_map[node.freq].head, node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._update_freq(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:

        # update value, increase freq and change location
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq(node)

        # If not present first check the present capacity if full remove node from min_freq list the rear one.
        # And, then add new node at the fornt of min_freq list.
        else:
            if len(self.cache) == self.capacity:
                min_freq_list = self.freq_map[self.min_freq]
                del self.cache[min_freq_list.tail.prev.key]
                min_freq_list.remove(min_freq_list.tail.prev)

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.freq_map[1].insert(self.freq_map[1].head, new_node)
            self.min_freq = 1


ope = [
    "LFUCache",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "put",
    "get",
    "get",
    "get",
]
cache = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

from collections import OrderedDict, defaultdict


class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.nodeCounts = defaultdict(OrderedDict)
        self.min = None

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]
        del self.nodeCounts[node.count][key]

        # If no element in bucket then remove that bucket
        if not self.nodeCounts[node.count]:
            del self.nodeCounts[node.count]

        # if node is found then increase it's cunt
        node.count += 1
        # Then we'll access that bucket and enter this node
        self.nodeCounts[node.count][key] = node

        # If minimum count of process is exceded then increase it
        if not self.nodeCounts[self.min]:
            self.min += 1

        return node.val

    def put(self, key: int, value: int) -> None:

        if not self.cap:
            return None

        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return

        if len(self.cache) == self.cap:
            lfu, _ = self.nodeCounts[self.min].popitem(last=False)
            del self.cache[lfu]

        newNode = Node(value, 1)
        self.cache[key] = newNode
        self.nodeCounts[1][key] = newNode
        self.min = 1


# Driver code

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

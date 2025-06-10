# https://leetcode.com/problems/all-oone-data-structure/


class Node:
    def __init__(self, val, next=None, prev=None, bucket_id=-1):
        self.val = val
        self.next = next
        self.prev = prev
        self.bucket_id = bucket_id


class DoublyLL:
    def __init__(self):
        self.left = Node(-1)  # Dummy head
        self.right = Node(-1)  # Dummy tail
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node):
        node.next = self.left.next
        node.prev = self.left
        self.left.next.prev = node
        self.left.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_empty(self):
        return self.left.next == self.right


class AllOne:
    def __init__(self):
        self.cache = {}  # key -> node
        self.bucket = {}  # bucket_id -> DoublyLL

    def inc(self, key: str) -> None:
        if key not in self.cache:
            node = Node(key)
            self.cache[key] = node
            node.bucket_id = 1
            if 1 not in self.bucket:
                self.bucket[1] = DoublyLL()
            self.bucket[1].add(node)
        else:
            node = self.cache[key]
            bucket_id = node.bucket_id
            self.bucket[bucket_id].remove(node)
            if self.bucket[bucket_id].is_empty():
                del self.bucket[bucket_id]
            bucket_id += 1
            node.bucket_id = bucket_id
            if bucket_id not in self.bucket:
                self.bucket[bucket_id] = DoublyLL()
            self.bucket[bucket_id].add(node)

    def dec(self, key: str) -> None:
        if key not in self.cache:
            return

        node = self.cache[key]
        bucket_id = node.bucket_id
        self.bucket[bucket_id].remove(node)

        if self.bucket[bucket_id].is_empty():
            del self.bucket[bucket_id]

        if bucket_id == 1:
            del self.cache[key]
        else:
            bucket_id -= 1
            node.bucket_id = bucket_id
            if bucket_id not in self.bucket:
                self.bucket[bucket_id] = DoublyLL()
            self.bucket[bucket_id].add(node)

    def getMaxKey(self) -> str:
        if not self.bucket:
            return ""
        max_bucket = max(self.bucket.keys())
        return self.bucket[max_bucket].left.next.val

    def getMinKey(self) -> str:
        if not self.bucket:
            return ""
        min_bucket = min(self.bucket.keys())
        return self.bucket[min_bucket].left.next.val


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

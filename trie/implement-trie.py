# https://leetcode.com/problems/implement-trie-prefix-tree/description/
class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        curr = self.head
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.head
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w]
        return True

obj = Trie()
obj.insert("apple")
print(obj.search("apple"))  # True
print(obj.search("app"))    # False
print(obj.startsWith("app"))  # True
print(obj.insert("app"))    # None
print(obj.search("app"))    # True
print(obj.startsWith("appl"))  # True
print(obj.startsWith("banana"))  # False

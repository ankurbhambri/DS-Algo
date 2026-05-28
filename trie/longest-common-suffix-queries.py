# https://leetcode.com/problems/longest-common-suffix-queries/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.length = float('inf')


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def update(self, node, idx, word):

        l = len(word)

        if l < node.length or (l == node.length and idx < node.idx):
            node.length = l
            node.idx = idx

    def insert(self, word, idx):

        node = self.root

        self.update(node, idx, word)

        for ch in reversed(word):

            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

            self.update(node, idx, word)

    def query(self, word):

        node = self.root

        for ch in reversed(word):

            if ch not in node.children:
                break

            node = node.children[ch]

        return node.idx


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        trie = Trie()

        for i, word in enumerate(wordsContainer):
            trie.insert(word, i)

        return [trie.query(word) for word in wordsQuery]


print(Solution().stringIndices(["aaa", "aa", "a"], ["aaaa", "aaa", "aa", "a"]))  # [-1, 0, 1, 2]
print(Solution().stringIndices(["aba", "baba", "aba", "xzxb"], ["aba", "baba", "xzxb", "ab"]))  # [2, 1, 3, -1]
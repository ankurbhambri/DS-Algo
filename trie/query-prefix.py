'''
Implement a function that, given a collection of words and a query prefix, returns all words that start with the given prefix.

Example:
    words = ["abc", "abd", "abef", "xyz"]
    prefix = "ab"

Output: ["abc", "abd", "abef"]
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_word = True


def find_words_with_prefix(words, prefix):

    trie = Trie()

    for word in words:
        trie.insert(word)

    node = trie.root

    for ch in prefix:
        if ch not in node.children:
            return []
        node = node.children[ch]

    result = []
    def dfs(curr, path):

        if curr.is_word:
            result.append(path)

        for ch, nxt in curr.children.items():
            dfs(nxt, path + ch)

    dfs(node, prefix)

    return result


print(find_words_with_prefix(["abc", "abd", "xyz"], "ab"))  # Output: ["abc", "abd"]
print(find_words_with_prefix(["hello", "hi", "hey", "world"], "he"))  # Output: ["hello", "hey"]
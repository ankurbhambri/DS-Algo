# https://leetcode.com/problems/longest-common-suffix-queries/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.length = float('inf')


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Jab bhi hum insert karenge, hum check karenge ki kya current word ka length existing length se chota hai ya nahi. 
    # Agar chota hai, toh hum update karenge. Agar length same hai, toh hum index check karenge aur chota index update karenge. 
    # Isse hume longest common suffix ke sath sath uska index bhi mil jayega.

    # Isse benifit ye hoga ki jab hum query karenge, toh hume longest common suffix ka index directly mil jayega bina extra traversal ke.
    def update(self, node, idx, word):

        l = len(word)

        if l < node.length or (l == node.length and idx < node.idx):
            node.length = l
            node.idx = idx

    # insert function mein hum word ko reverse order mein insert karenge taki hum longest common suffix ke hisab se trie banayein.
    def insert(self, word, idx):

        node = self.root

        self.update(node, idx, word)

        for ch in reversed(word):

            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

            self.update(node, idx, word)

    # query function mein hum word ko reverse order mein traverse karenge aur trie mein check karenge ki kya current node ke length aur index valid hain ya nahi.
    def query(self, word):

        node = self.root

        for ch in reversed(word):

            if ch not in node.children:
                return -1

            node = node.children[ch]

        return node.idx


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        trie = Trie()

        # Step 1: Trie mein saare words ko insert karo
        for i, word in enumerate(wordsContainer):
            trie.insert(word, i)

        # Step 2: Har query ke liye longest common suffix ka index find karo
        return [trie.query(word) for word in wordsQuery]


print(Solution().stringIndices(["aaa", "aa", "a"], ["aaaa", "aaa", "aa", "a"]))  # [-1, 0, 1, 2]
print(Solution().stringIndices(["aba", "baba", "aba", "xzxb"], ["aba", "baba", "xzxb", "ab"]))  # [2, 1, 3, -1]
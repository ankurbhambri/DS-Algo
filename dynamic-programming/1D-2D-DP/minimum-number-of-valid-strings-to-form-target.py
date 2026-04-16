# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

class TrieNode:
    def __init__(self):
        self.children = {}

# TC: O(n * m) where n is the length of target and m is the average length of words in the Trie
# SC: O(n) for the DP array and O(total characters in words) for the Trie, which is manageable given the constraints.
class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:

        # Step 1: Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

        n = len(target)
        # Step 2: DP array initialized with infinity
        dp = [float('inf')] * (n + 1)
        dp[n] = 0 # Base case

        # Step 3: Fill DP from right to left
        for i in range(n - 1, -1, -1):
            node = root
            # Target[i] se start hone wale saare valid prefixes check karo
            for j in range(i, n):
                if target[j] in node.children:
                    node = node.children[target[j]]
                    # Agar i se j tak ek valid prefix mila
                    dp[i] = min(dp[i], 1 + dp[j + 1])
                else:
                    # Agar Trie mein rasta khatam, toh aage koi prefix nahi milega
                    break

        return dp[0] if dp[0] != float('inf') else -1


words = ["abc","aaaaa","bcdef"]
target = "aabcdabc"
print(Solution().minValidStrings(words, target))
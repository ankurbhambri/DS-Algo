# https://leetcode.com/problems/longest-common-prefix/


# TC: O(S) where S is the sum of all characters in all strings
# SC: O(S) where S is the sum of all characters in all strings
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        trie = {}

        for word in strs:
            curNode = trie
            for char in word:
                if char not in curNode:
                    curNode[char] = {}
                curNode = curNode[char]
            curNode["*"] = {}

        curPre = ""
        curNode = trie

        while len(curNode) == 1 and "*" not in curNode:
            for key in curNode:
                curNode = curNode[key]
                curPre += key

        return curPre

print(Solution().longestCommonPrefix(["apple", "apps", "ape"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
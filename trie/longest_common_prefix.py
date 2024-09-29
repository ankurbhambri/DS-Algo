# https://leetcode.com/problems/longest-common-prefix/


# Using Trie


def longestCommonPrefix(strs):
    trie = {}

    for word in strs:
        curNode = trie
        for char in word:
            if char not in curNode:
                curNode[char] = {}
            curNode = curNode[char]
        curNode["*"] = {}

    curNode = trie
    curPre = ""

    while len(curNode) == 1 and "*" not in curNode:
        for key in curNode:
            curNode = curNode[key]
            curPre += key

    return curPre


print(longestCommonPrefix(["flower", "flow", "flight"]))

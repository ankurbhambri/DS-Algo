# https://leetcode.com/problems/word-search/description/

def exist(board, word):

    r, c = len(board), len(board[0])

    def dfs(i, j, idx):

        if idx == len(word):
            return True

        if (min(i, j) < 0 or i >= r or j >= c or word[idx] != board[i][j] or board[i][j] == "$"):
            return False

        tmp = board[i][j]
        board[i][j] = "$"

        res = (
            dfs(i + 1, j, idx + 1)
            or dfs(i - 1, j, idx + 1)
            or dfs(i, j + 1, idx + 1)
            or dfs(i, j - 1, idx + 1)
        )

        board[i][j] = tmp

        return res

    for i in range(r):
        for j in range(c):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False

print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))  # True


# https://leetcode.com/problems/word-search-ii/description/

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)  # Dictionary for next characters
        self.word = None  # Store word if this is end of a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                node = node.children[char]  # Move to next node or create new
            node.word = word  # Mark end of word
        
        m, n = len(board), len(board[0])
        res = []
        
        def dfs(i: int, j: int, node: TrieNode, visited: set):

            # boundaries hit or char doesn't exists in Trie
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or board[i][j] not in node.children:
                return
            
            # Move to next Trie node
            curr_char = board[i][j]
            next_node = node.children[curr_char]
            
            # If we found a word, add to res
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # Remove word to avoid duplicates
            
            # Mark current cell as visited
            visited.add((i, j))
            
            # Explore all four directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj, next_node, visited)
            
            # Unmark cell after exploration (backtracking)
            visited.remove((i, j))
            
            # Optimization step: Remove empty Trie branches to reduce future searches.
            if not next_node.children and not next_node.word:
                del node.children[curr_char]
        
        # Step 3: Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, set())
        
        return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(Solution().findWords(board, words))  # ["eat","oath"]


# from collections import defaultdict

# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)  # Dictionary for next characters
#         self.word = None  # Store word if this is end of a word

# # Building Trie
# root = TrieNode()
# words = ["oath", "pea", "eat", "rain", "apple", "apply", "applet"]
# for word in words:
#     node = root
#     for char in word:
#         node = node.children[char]  # Move to next node or create new
#     node.word = word  # Mark end of word

# print(root)
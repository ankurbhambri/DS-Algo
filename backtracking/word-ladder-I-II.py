# https://leetcode.com/problems/word-ladder/description/

from collections import deque, defaultdict

def ladderLength(beginWord, endWord, wordList):

        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        # Use deque for efficient queue operations
        q = deque([beginWord])
        visited = set([beginWord])
        level = 1  # Start with 1 since beginWord is included

        # Precompute patterns

        ######################################################

        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_dict[pattern].append(word)

        def getNei(word):
            nei = []
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei.extend(pattern_dict[pattern])
            return nei
        
        ############################## Just for creating neighbour words
        
        # Alternative getNei function without precomputation, but less efficient
        # def getNei(word):
        #     nei = []
        #     for i in range(len(word)):
        #         for j in range(26):
        #             ch = chr(ord('a') + j)
        #             if ch == word[i]:
        #                 continue
        #             tmp = word[:i] + ch + word[i+1:]
        #             if tmp in wordList:
        #                 nei.append(tmp)
        #     return nei
        
        while q:
            for _ in range(len(q)):  # Process level by level
                node = q.popleft()  # Pop from front for BFS
                if node == endWord:
                    return level
                
                for nei in getNei(node):
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            
            level += 1
        
        return 0


# https://leetcode.com/problems/word-ladder-ii/description/


def findLadders(beginWord, endWord, wordList):
    # Convert wordList to set for O(1) lookup
    wordList = set(wordList)
    if endWord not in wordList:
        return []
    
    # Precompute patterns for neighbors
    pattern_dict = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            pattern_dict[pattern].append(word)
    
    # Add beginWord to pattern_dict if it's not in wordList
    if beginWord not in wordList:
        for i in range(len(beginWord)):
            pattern = beginWord[:i] + "*" + beginWord[i+1:]
            pattern_dict[pattern].append(beginWord)
    
    def getNeighbors(word):
        neighbors = []
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            neighbors.extend(pattern_dict[pattern])
        return [n for n in neighbors if n != word]
    
    # BFS to build parent graph
    parents = defaultdict(list)  # Store parent -> child relationships
    level = {beginWord: 0}  # Track level of each word
    queue = deque([(beginWord, 0)])  # (word, level)
    visited = {beginWord}  # Track visited words
    end_level = float('inf')  # To stop BFS once endWord is found
    
    while queue:
        curr_word, curr_level = queue.popleft()
        if curr_level >= end_level:
            break
            
        for neighbor in getNeighbors(curr_word):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, curr_level + 1))
                level[neighbor] = curr_level + 1
                parents[neighbor].append(curr_word)
            elif level[neighbor] == curr_level + 1:
                parents[neighbor].append(curr_word)
        
        if curr_word == endWord:
            end_level = curr_level
    
    if endWord not in level:
        return []
    
    # Backtrack to find all paths
    result = []
    def backtrack(word, path):
        if word == beginWord:
            result.append(path[::-1])
            return
        for parent in parents[word]:
            backtrack(parent, path + [parent])
    
    backtrack(endWord, [endWord])
    return result


print(findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

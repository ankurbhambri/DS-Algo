# https://leetcode.com/problems/word-ladder/

from collections import deque

# TC: O(N * M^2) where N is the number of words in the wordList and M is the length of each word. 
# For each word, we generate M patterns and for each pattern, we may have to check all N words.
# SC: O(N * M) for storing the patterns in the dictionary.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        wordSet = set(wordList) 
        
        # Agar target word list mein hi nahi hai, toh pahunchne ka koi rasta nahi hai
        if endWord not in wordSet:
            return 0 

        # Shuruat mein beginWord aur step count 1 hoga
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, steps = queue.popleft()
            
            # Agar hum target word par pahunch gaye, toh steps return kar do
            if current_word == endWord:
                return steps
                
            # Ab current_word ke har ek character ko 'a' se 'z' tak badal kar check karenge
            for i in range(len(current_word)):

                original_char = current_word[i]
                
                for c in 'abcdefghijklmnopqrstuvwxyz':

                    if c == original_char:
                        continue # Agar same character hai toh skip karo

                    # Naya word banaya ek character badal kar
                    next_word = current_word[:i] + c + current_word[i+1:]

                    # Agar naya word dictionary (wordSet) mein maujood hai
                    if next_word in wordSet:

                        # Use set se remove kar dete hain taaki loop mein dobara na aaye (visited list ki tarah)
                        wordSet.remove(next_word)

                        # Queue mein agle step ke liye daal dete hain
                        queue.append((next_word, steps + 1))
                        
        return 0 # Agar queue khali ho gayi aur target nahi mila, matlab rasta nahi hai


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # Output: 5
print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # Output: 0


# https://leetcode.com/problems/word-ladder-ii/description/

# TC: O(N * M^2) where N is the number of words in the wordList and M is the length of each word.
# SC: O(N * M) for storing the patterns in the dictionary.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return [] # Target word agar list mein nahi hai toh khali list return karo
            
        # STEP 1: BFS se har word ka shortest distance nikalna beginWord se
        dist = {beginWord: 0} # {word: distance_from_beginWord}
        queue = deque([beginWord])
        
        # Visited track karne ke liye hum set se direct tabhi remove karenge jab wo level khatam ho
        if beginWord in wordSet:
            wordSet.remove(beginWord)
            
        found = False
        while queue and not found:

            visited_this_level = set()

            # Ek poore level ko ek sath process karenge
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                
                if curr_word == endWord:
                    found = True
                    break
                    
                # Har character ko badal kar check karo
                for i in range(len(curr_word)):
                    original_char = curr_word[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original_char:
                            continue
                        next_word = curr_word[:i] + c + curr_word[i+1:]
                        
                        if next_word in wordSet:
                            if next_word not in dist:
                                dist[next_word] = dist[curr_word] + 1
                                queue.append(next_word)
                                visited_this_level.add(next_word)
                                
            # Level ke saare words ko ab main set se remove kar do taaki agle level par reuse na ho
            for word in visited_this_level:
                wordSet.remove(word)
                
        # Agar target tak pahunchne ka koi rasta nahi mila
        if endWord not in dist:
            return []
            
        # STEP 2: DFS/Backtracking (Target se ulta beginWord ki taraf aana)
        ans = []
        
        def dfs(curr_word, path):
            # Base case: Jab ulta chalte hue beginWord par pahunch gaye
            if curr_word == beginWord:
                ans.append(path[::-1]) # Path ko sidha karke answer mein daal do
                return
                
            # Current word se 1 step piche ke saare possible words check karo
            for i in range(len(curr_word)):
                original_char = curr_word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                    prev_word = curr_word[:i] + c + curr_word[i+1:]
                    
                    # Agar yeh prev_word BFS ke raste mein tha aur iska distance exactly 1 kam hai
                    if prev_word in dist and dist[prev_word] == dist[curr_word] - 1:
                        path.append(prev_word)
                        dfs(prev_word, path)
                        path.pop() # Backtrack (taki dusra rasta check ho sake)

        # DFS shuru karo endWord se, path mein endWord pehle se hoga
        dfs(endWord, [endWord])
        return ans


print(findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

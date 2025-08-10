 # https://leetcode.com/problems/palindrome-partitioning/

# Question: Given a string s, partition s such that every substring of the partition is a palindrome.

# Tc: O(n * 2^n)
# SC:  O(n) (stack) + O(2^n * n) (output)
class Solution:
    def partition(self, s):
        
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):

            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub): # condition to check if substring is palindrome
                    path.append(sub)
                    backtrack(end, path)
                    path.pop() # backtrack to explore other partitions

        backtrack(0, [])
        return res


print(Solution().partition("aab"))  # [['a', 'a', 'b'], ['aa', 'b']]
print(Solution().partition("a"))  # [['a']]
print(Solution().partition("racecar"))  # [['r', 'a', 'c', 'e', 'c', 'a', 'r'], ['r', 'a', 'c', 'e', 'c', 'a', 'r']]
print(Solution().partition("ab"))  # [['a', 'b']]

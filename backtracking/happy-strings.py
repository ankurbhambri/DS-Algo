# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n

'''
 
A string is called happy if it consists only of the characters 'a', 'b', and 'c', 
and no two consecutive characters are the same. For example, "abc" and "aba" are happy strings, but "aa" and "ad" are not.

'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        tmp = []

        def backtrack(path):

            if len(path) == n:
                tmp.append("".join(path))
                return

            for ch in ("a", "b", "c"):

                if path and path[-1] == ch:
                    continue

                path.append(ch)
                backtrack(path)
                path.pop()

        backtrack([])

        return "" if len(tmp) <= k - 1 else tmp[k - 1]


print(Solution().getHappyString(1, 3))  # "c"
print(Solution().getHappyString(1, 4))  # ""
print(Solution().getHappyString(3, 9))  # "cab"
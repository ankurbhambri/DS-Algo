# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int):
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res


n = 4
k = 2
print(Solution().combine(n, k))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

n = 5
k = 3
print(Solution().combine(n, k))  # [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]

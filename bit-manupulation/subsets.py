# https://leetcode.com/problems/subsets/


# Backtracking approach

# Tc: O(n * 2^n)
# SC: O(n) + O(2^n * n)

class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            res.append(path[:])  # add every path (even empty)
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# Another approach using bit manipulation

# TC: O(n * 2^n)
# SC: O(n * 2^n)

class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []
        for i in range(2 ** n):
            tmp = []
            for j in range(n):
                print(1 << j, i & (1 << j))
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res

print(Solution().subsets([1, 2, 3]))  # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Another way for above problem

# TC: O(n * 2^n)
# SC: O(n * 2^n)

def subsets(nums):

    res = [[]]

    for num in nums:
        # [[]] * [1], [[], [1]] * [2] ........
        res += [i + [num] for i in res]

    return res

print(subsets([1, 2, 3]))  # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


# https://leetcode.com/problems/subsets-ii/


# Backtracking approach

# Tc: O(n * 2^n)
# SC: O(n) + O(2^n * n)

class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()  # required to handle duplicates

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # skip duplicate at same tree level
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# Another approach using bit manipulation

# TC: O(2^n * n log n)
# SC: O(n * 2^n)
class Solution:
    def subsetsWithDup(self, nums):

        n = len(nums)
        res = []
        seen = set()

        for i in range(2 ** n):
            tmp = []
            for j in range(n):
                if i & (1 << j):
                    tmp.append(nums[j])

            tmp.sort()
            if tuple(tmp) not in seen:
                res.append(tmp)
                seen.add(tuple(tmp))

        return res
    
print(Solution().subsetsWithDup([1, 2, 2]))  # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

# short code
class Solution:
    def distinctSubseqII(self, S):
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i

        return (dp[-1] - 1) % (10**9 + 7)

print(Solution().subsetsWithDup([1, 2, 2]))  # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

# https://leetcode.com/problems/subsets/

# TC: O(n * 2^n), SC: O(n * 2^n)
class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []
        for i in range(2 ** n):
            tmp = []
            for j in range(n):
                if i & (1 << j):
                    tmp.append(nums[j])
            res.append(tmp)
        return res

print(Solution().subsets([1, 2, 3]))  # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# another way for above problem
# TC: O(n * 2^n), SC: O(n * 2^n)
def subsets(nums):
    res = [[]]

    for num in nums:
        # [[]] * [1], [[], [1]] * [2] ........
        res += [i + [num] for i in res]

    return res

print(subsets([1, 2, 3]))  # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


# https://leetcode.com/problems/subsets-ii/

# TC: O(2^n * n log n) and SC: O(n * 2^n)
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

# https://leetcode.com/problems/permutations/description/


# Narayana Pandita Technique

# This technique works for both I and II problems

def permute(nums):

    # Step 1: Array ko sort karein (Smallest permutation)
    nums.sort()
    res = []
    res.append(list(nums))

    # Step 2: Jab tak humein "Next Permutation" milti rahegi, loop chalega
    while True:

        # 1. Pivot dhundo
        k = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break

        # Agar k == -1, matlab saari permutations ho chuki hain (Descending order reached)
        if k == -1:
            break

        # 2. Successor dhundo
        l = -1
        for i in range(len(nums) - 1, k, -1):
            if nums[i] > nums[k]:
                l = i
                break

        # 3. Swap
        nums[k], nums[l] = nums[l], nums[k]

        # 4. Reverse the tail
        nums[k+1:] = reversed(nums[k+1:])

        # Result mein current arrangement add karein
        res.append(list(nums))

    return res

# Another way easy to understand but not space efficient

# Backtracking Approach

class Solution:
    def permute(self, nums):

        res = []

        def backtrack(start):

            # Base Case: Agar hum aakhri index tak pahunch gaye
            if start == len(nums):
                res.append(nums[:]) # nums ki copy add karein
                return

            for i in range(start, len(nums)):
                # 1. Swap: Current element ko start position par laao
                nums[start], nums[i] = nums[i], nums[start]

                # 2. Explore: Baaki bache hue array ke liye recursion chalao
                backtrack(start + 1)

                # 3. Backtrack: Wapas swap karke original state mein laao
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res

print(Solution().permute([0, 1]))  # [[0, 1], [1, 0]]     
print(Solution().permute([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


# BFS Approach

from collections import deque

class Solution:
    def permute(self, nums):

        q = deque()
        q.append(((nums, [])))

        res = []

        while q:

            nums, path = q.popleft()

            if not nums:
                res.append(path)

            for i in range(len(nums)):

                newNums = nums[:i] + nums[i+1:]
                q.append((newNums, path + [nums[i]]))

        return res

print(Solution().permute([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] 
print(Solution().permute([0, 1]))  # [[0, 1], [1, 0]]
print(Solution().permute([1]))  # [[1]]
print(Solution().permute([]))  # [[]]
print(Solution().permute([1, 2, 3, 4]))  # All permutations of [1, 2, 3, 4]
print(Solution().permute([5, 6, 7]))  # All permutations of [5, 6, 7]


# https://leetcode.com/problems/permutations-ii/description/

# Only difference is from above is to return unique permutations
class Solution:
    def permuteUnique(self, nums):

        q = deque()
        q.append(((nums, [])))

        res = set()

        while q:

            nums, path = q.popleft()

            if not nums:
                res.add(tuple(path))

            for i in range(len(nums)):

                newNums = nums[:i] + nums[i+1:]
                q.append((newNums, path + [nums[i]]))

        return list(res)
    

print(Solution().permuteUnique([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] 
print(Solution().permuteUnique([0, 1]))  # [[0, 1], [1, 0]]
print(Solution().permuteUnique([1]))  # [[1]]
print(Solution().permuteUnique([]))  # [[]]
print(Solution().permuteUnique([1, 2, 3, 4]))  # All permutations of [1, 2, 3, 4]
print(Solution().permuteUnique([5, 6, 7]))  # All permutations of [5, 6, 7]

# https://leetcode.com/problems/house-robber/


# Intution:

'''

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    return dp[-1]

    
Example  nums = [2,7,9,3,1]

# dp[i] = max(dp[i-1], nums[i] + dp[i-2])

dp[0] = 2 (first house).
dp[1] = max(2, 7) = 7 (first or second house).
i=2: dp[2] = max(dp[1], nums[2] + dp[0]) = max(7, 9+2) = 11.
i=3: dp[3] = max(dp[2], nums[3] + dp[1]) = max(11, 3+7) = 11.
i=4: dp[4] = max(dp[3], nums[4] + dp[2]) = max(11, 1+11) = 12.
........

But here we don't need to store the entire dp array, we can just keep track of the last two values.


rob1 = dp[i-2]
rob2 = dp[i-1]

rob this house, add value of skipping previous (nums[i] + dp[i-2])
skip this house, keep max up to previous house (dp[i-1])

'''

class Solution:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2

# money in the houses
print(Solution().rob([1, 2, 3, 1]))  # 4


# https://leetcode.com/problems/house-robber-ii/
class Solution:

    # similar to House Robber I, but we need to handle the circular nature of the houses.
    def rob(self, nums) -> int:
        
        def helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(n + rob1, rob2)
            return rob2

        # skip the first or the last house
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


print(Solution().rob([1, 2, 3, 1]))  # 4


# https://leetcode.com/problems/house-robber-iii/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode):
        def dfs(node):
            if not node:
                return [0, 0]  # [include, exclude]
            
            # Left aur right subtree ke results
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Include case: node ka value + left exclude + right exclude
            include = node.val + left[1] + right[1]
            
            # Exclude case: max of (left include, left exclude) + max of (right include, right exclude)
            exclude = max(left[0], left[1]) + max(right[0], right[1])
            
            return [include, exclude]
        
        result = dfs(root)
        return max(result[0], result[1])

obj = TreeNode(3)
obj.left = TreeNode(2)
obj.right = TreeNode(3)
obj.left.right = TreeNode(3)
obj.right.right = TreeNode(1)
print(Solution().rob(obj))  # 7


# https://leetcode.com/problems/house-robber-iv/ 

# Binary search + Greedy approach

'''
Understand the Goal:
- You need to find the minimum capability (maximum amount you can rob from any house) such that you can rob exactly k houses.
- You cannot rob adjacent houses (same as House Robber I).

Key Constraint:
- Capability is a limit: you can only rob houses where the amount is less than or equal to the capability.
- The answer is the smallest capability that allows you to rob at least k houses.

Binary Search Approach:
- The capability must be between min(nums) and max(nums) (minimum and maximum values in the array).
- Use binary search to find the smallest capability that satisfies the condition of robbing at least k houses.

Check Function:
- For a given capability (mid), check if you can rob at least k houses:
    1. Traverse the array greedily.
    2. If nums[i] <= mid, rob the house and skip the next one (i += 2).
    3. Count the number of houses robbed.
    4. Return true if count >= k, else false.

Binary Search Logic:
- If the check function returns true, the capability is valid, but try a smaller one (move right boundary to mid).
- If the check function returns false, you need a larger capability (move left boundary to mid + 1).
- When left == right, you’ve found the minimum capability.

Greedy Traversal:
- When checking a capability, use a greedy approach to maximize the number of houses robbed (while respecting the no-adjacent rule).
- This ensures you know if the current capability can achieve at least k houses.

Time Complexity:
- Binary search: O(log M), where M is max(nums) - min(nums).
- Check function: O(n) for each traversal.
- Total: O(n * log M).

Space Complexity:
- O(1), as only a few variables are used (no extra arrays).
'''

class Solution:
    def minCapability(self, nums, k):
        def canRobK(mid: int) -> bool:
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 2  # Skip adjacent house
                else:
                    i += 1
            return count >= k
        
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRobK(mid):
                right = mid  # Try smaller capability
            else:
                left = mid + 1  # Need larger capability
        return left


print(Solution().minCapability([2, 3, 5, 9], 2))  # 5
print(Solution().minCapability([2, 7, 9, 3, 1], 2))  # 2

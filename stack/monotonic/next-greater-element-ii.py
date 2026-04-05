# https://leetcode.com/problems/next-greater-element-ii/

'''
Loop once, we can get the Next Greater Number of a normal array.
Loop twice, we can get the Next Greater Number of a circular array

Complexity
    Time O(N) for one pass
    Space O(N) in worst case
'''

class Solution:
    def nextGreaterElements(self, nums):

        stack = []
        res = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        return res


print(Solution().nextGreaterElements([1,2,1]))  # Output: [2,-1,2]
print(Solution().nextGreaterElements([1,2,3,4,3]))  # Output: [2,3,4,-1,-1]
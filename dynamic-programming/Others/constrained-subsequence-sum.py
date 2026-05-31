# https://leetcode.com/problems/constrained-subsequence-sum/

from collections import deque

# TC: O(n)
# SC: O(n)

'''
Idea

Here, queue is used to track the max sum at what index so far 

dp is actually storing the max sum and using the max value to sum with ongoing values

like first 10 will go in dp and 0 will go in queue
then 2 will add in 10 and dp will store 12 and queue first pop the 10 and store the index 1 becasue till index 1 we have the max
then for -10 dp will add the max value based on index store is queue (monotonic descresing), will give the max value of dp and add

then check value if gt to the exxisting if not skip and so on

then 5 will come, add with the max value in the dp, index will get from queue at first and add 5 will give 17, start removing samll values

then 20 will be added with 17 and become 37, thansk to queue for storing the index, which is having max value in dp.

'''

class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:

        queue = deque()
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            if queue and i - queue[0] > k:
                queue.popleft()
            
            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            
            if dp[i] > 0:
                queue.append(i)
                
        return max(dp)

print(Solution().constrainedSubsetSum([10, 2, -10, 5, 20], 2))  # Output: 37
print(Solution().constrainedSubsetSum([-1, -2, -3], 1))  # Output: -1
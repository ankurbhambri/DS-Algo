# https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1

# Question: Given an array of integers and a number k, find the first negative integer for each and every window (subarray) of size k.
# If a window does not contain a negative integer, then return 0 for that window.


from collections import deque


# Time Complexity: O(n)
# Space Complexity: O(k) for the deque
class Solution:
    def firstNegInt(self, nums, k):

        q = deque()  # stores indices of negative numbers
        res = []
    
        for i in range(len(nums)):
            # add current negative to queue
            if nums[i] < 0:
                q.append(i)
            
            # remove out-of-window negatives
            if q and q[0] <= i - k:
                q.popleft()
            
            # start recording answers only when we have k elements processed
            if i >= k - 1:
                res.append(nums[q[0]] if q else 0)

        return res


print(Solution().firstNegInt([12, -1, -7, 8, -15, 30, 16, 28], 3))  # [-1, -1, -7, -15, -15, 0]
print(Solution().firstNegInt([1, 2, 3, -4, 5, -6, 7, 8], 2))  # [0, 0, -4, -4, -6, -6, 0]
print(Solution().firstNegInt([-1, -2, -3, -4, -5], 1))  # [-1, -2, -3, -4, -5]
print(Solution().firstNegInt([1, 2, 3, 4, 5], 2))  # [0, 0, 0, 0]
print(Solution().firstNegInt([0, 0, 0, 0], 3))  # [0, 0]

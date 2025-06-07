# https://leetcode.com/problems/longest-increasing-subsequence/

"""
    The idea here, We start with a dp array of length equal to the number of elements in the input array, nums.

    We initialize each element of the dp array to 1, as the minimum length of any subsequence is 1 for itself.

    First start iterate, check the previous elements (from 0 to i-1) and check if the current element is greater than the previous element.

    If it is, we update the dp array at index i with the maximum value between its current value and 1 plus the dp value at the previous index.


"""

# TC: O(n^2)
# SC: O(n)
def lengthOfLIS(nums):

    dp = [1] * len(nums)

    for i in range(1, len(nums)):  # -> i to len(nums)
        for j in range(i):  # -> 0 to i
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
print(lengthOfLIS([4, 10, 4, 3, 8, 9]))  # 3
print(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6

import bisect

"""
    The idea here is to use binary search to solve the problem.
    We start with an empty list, sub, which will store the smallest tail of all increasing subsequences of different lengths.

    For each element in the input array, we perform a binary search on the sub list to find the index where the current element can be placed.
    If the index is equal to the length of the sub list, it means that the current element is greater than all elements in sub, so we append it to sub.
    Otherwise, we replace the element at that index with the current element.

    Finally, we return the length of the sub list, which represents the length of the longest increasing subsequence in the nums array.

    TC: O(n log n)
    SC: O(n)
"""

def lengthOfLIS(nums):

    sub = []  # this stores the smallest last values of increasing subsequences

    for num in nums:
        # Find index of the first element in sub that is >= num
        idx = bisect.bisect_left(sub, num)
        
        if idx == len(sub):
            # num is bigger than all elements in sub, so it extends LIS
            sub.append(num)
        else:
            # num can replace an existing element to keep sub minimal
            sub[idx] = num

    return len(sub)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
print(lengthOfLIS([4, 10, 4, 3, 8, 9]))  # 3
print(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6


# Print longest increasing subsequence
def printLIS(nums):

    n = len(nums)

    dp = [1] * n

    parent = [-1] * n  # to reconstruct path

    max_len = 1
    max_index = 0

    # Fill dp and parent arrays
    for i in range(n):
        for j in range(i):

            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:

                dp[i] = dp[j] + 1
                parent[i] = j
        
        # Track the overall max LIS length and its ending index
        if dp[i] > max_len:
            max_len = dp[i]
            max_index = i

    # Reconstruct LIS
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = parent[max_index]

    lis.reverse()
    return lis


print(printLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: [2, 3, 7, 101]
print(printLIS([0, 1, 0, 3, 2, 3]))  # Output: [0, 1, 2, 3]
print(printLIS([7, 7, 7, 7, 7, 7]))  # Output: [7]
print(printLIS([]))  # Output: []

# Similar question - https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii

class Solution:
    def getWordsInLongestSubsequence(self, words, groups):

        n = len(groups)

        dp = [1] * n
        prev = [-1] * n
        max_len = 1
        max_index = 0

        def check(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
            return True       

        for i in range(1, n):
            for j in range(i):

                if (groups[i] != groups[j] and dp[i] < dp[j] + 1 and check(words[i], words[j])):

                    dp[i] = dp[j] + 1

                    prev[i] = j # Store the previous index, that was smaller

            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        res = []
        while max_index != -1: # Backtrack to find the longest increasing subsequence
            res.append(words[max_index])
            max_index = prev[max_index]

        res.reverse() # Reverse the result to get the correct order
        return res

print(Solution().getWordsInLongestSubsequence(["bab","dab","cab"], [1, 2, 2]))  # Output: ["bab","cab"]
print(Solution().getWordsInLongestSubsequence(["a","b","c","d"], [1, 2, 3, 4]))  # Output: ["a","b","c","d"]

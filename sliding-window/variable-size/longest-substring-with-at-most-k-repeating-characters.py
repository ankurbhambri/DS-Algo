"""
    https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

    Given a string s, find the length of the longest substring T that contains at most k distinct characters.

    Note - same as above replace static value 2 with k only

    Similar question - https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/ replace k with 2

"""

# 2461. Maximum Sum of Distinct Subarrays With Length K

# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/


def maximumSubarraySum(nums, k):
    l = 0
    seen = set()
    sm = 0
    res = 0

    for r in range(len(nums)):
        sm += nums[r]

        while nums[r] in seen or (r - l + 1) > k:

            seen.remove(nums[l])
            sm -= nums[l]
            l += 1

        seen.add(nums[r])

        if r - l + 1 == k:
            res = max(res, sm)

    return res


print(maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))  # 15
print(maximumSubarraySum([1, 2, 1, 2, 3], 2))  # 4
print(maximumSubarraySum([1, 2, 1, 3, 4], 3))  # 7

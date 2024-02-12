"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(s):

        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res

    # same for array as well
    # https://leetcode.com/problems/maximum-erasure-value/


def maximumUniqueSubarray(s):
    charSet = set()

    l = 0
    res = 0
    sm = 0

    for r in range(len(s)):

        sm += s[r]

        while s[r] in charSet:
            sm -= s[l]
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        res = max(res, sm)

    return res


"""
    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

    Given a string S, find the length of the longest substring T that contains at most k distinct characters.

    Note - same as above replace static value 2 with k only

    Similar question - https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/ replace k with 2

"""


class Solution:

    def length_of_longest_substring_k_distinct(s, k):
        l = 0
        res = 0
        freq = dict()

        for r in range(len(s)):

            freq[s[r]] = 1 + freq.get(s[r], 0)

            while len(freq) > k:

                freq[s[l]] -= 1

                l += 1

                if freq[s[l]] == 0:

                    del freq[s[l]]

            # windows length always calculated from (r - l + 1)
            res = max(res, r - l + 1)

        return res


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

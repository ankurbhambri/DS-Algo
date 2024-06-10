"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

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


def maximumUniqueSubarray(self, s: List[int]) -> int:
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
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Given a string, find the length of the longest substring S that contains at most 2 distinct characters.

"""


class Solution:
    def length_of_longest_substring_two_distinct(self, s: str) -> int:

        l = 0
        res = 0
        freq = dict()

        for r in range(len(s)):
            w = s[r]

            # calculating frequency here of all characters
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1

            while len(freq) > 2:
                wl = s[l]

                freq[wl] -= 1

                l += 1

                if freq[wl] == 0:

                    del freq[wl]

            res = max(res, r - l + 1)

        return res


"""
    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

    Given a string S, find the length of the longest substring T that contains at most k distinct characters.

    Note - same as above replace static value 2 with k only

"""


class Solution:

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = dict()

        for r in range(len(s)):
            w = s[r]
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
            while len(freq) > k:
                wl = s[l]

                freq[wl] -= 1

                l += 1

                if freq[wl] == 0:

                    del freq[wl]

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

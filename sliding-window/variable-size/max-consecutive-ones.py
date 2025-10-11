# https://leetcode.com/problems/max-consecutive-ones-iii/

'''
    If the number of zeros in the window (zeros) exceeds k, the window is invalid (we can't flip more than k zeros).
    Shrink the window from the left (l) until zeros <= k:

    If nums[l] == 0, decrement zeros (since we're removing a zero from the window).
    Increment l to shrink the window.

    This ensures the window always has at most k zeros.
'''

class Solution:
    def longestOnes(self, nums, k: int) -> int:

        l = 0
        zeros = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


print(Solution().longestOnes([1,1,0,0,1,1,0,1], 2))  # Output: 6
print(Solution().longestOnes([0,0,1,1,0,0,1,1], 1))  # Output: 4
print(Solution().longestOnes([1,0,1,0,1,0], 3))  # Output: 6
print(Solution().longestOnes([1,1,1,1,1], 0))  # Output: 5


# Variant

'''

Given an m x n character matrix days of 'W' and 'H' where W represents a work day you may take off and H represents a holiday, 
return the longest possible vacation of consecutive days you can take if you are allowed at most PTO days off.

Example 1:

    Input: days = [['W', 'H', 'W'], ['H', 'W', 'H'], ['W', 'H', 'W']],
    PTO = 3
    Output: 7

Example 2:

    Input: days = [['W', 'H', 'H', 'W', 'W'], ['H', 'W', 'W', 'W', 'W']],
    PTO = 2
    Output: 5

Constraints:

    m == days. length
    • n == days [i]. length
    • 1 <= m <= 10^3
    • 1 <= n <= 10^3
    days[i][j] is either W or H.
    0 <= PTO <= 10^7

'''

def solution(days, pto):

    l = 0
    w = 0
    res = 0

    rows, cols = len(days), len(days[0])

    # traverse like a list with a single loop, we can flatten indexing: row = i // cols, col = i % cols
    def getIndex(idx):
        return days[idx // cols][idx % cols]

    n = rows * cols # flatten the matrix

    for i in range(n):

        if getIndex(i) == 'W':
            w += 1

        while w > pto:

            if getIndex(l) == 'W':
                w -= 1

            l += 1

        res = max(res, i - l + 1)

    return res


print(solution([['W', 'H', 'W'], ['H', 'W', 'H'], ['W', 'H', 'W']], 3))  # Output: 7
print(solution([['W', 'H', 'H', 'W', 'W'], ['H', 'W', 'W', 'W', 'W']], 2))  # Output: 5


# Variant: What if PTO is decimal? like: 2.5, or 3.2, In that case we can simply find the max window and a check from left or right side is 'W' day then add that decimal extension as well.

def solution(days, pto):

    l = 0
    w = 0
    res = 0

    pto_ext = pto - int(pto)  # integer part of PTO
    pto = int(pto)  # integer part of PTO

    rows, cols = len(days), len(days[0])

    n = rows * cols

    def getIndex(idx):
        return days[idx // cols][idx % cols]

    for i in range(n):

        if getIndex(i) == 'W':
            w += 1

        while w > pto:

            if getIndex(l) == 'W':
                w -= 1

            l += 1

        ext = 0.0
        if l > 0 and getIndex(l - 1) == 'W' or i < n - 1 and getIndex(i + 1) == 'W':
            ext = pto_ext

        res = max(res, i - l + 1 + ext)

    return res


print(solution([['W', 'H', 'W'], ['H', 'W', 'H'], ['W', 'H', 'W']], 3.5))  # Output: 7.5
print(solution([['W', 'H', 'W'], ['H', 'W', 'H'], ['W', 'H', 'H']], 4.5))  # Output: 9.0
print(solution([['W', 'H', 'H', 'W', 'W'], ['H', 'W', 'W', 'W', 'W']], 2.2))  # Output: 5.2
print(solution([['H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H']], 1.5))  # Output: 10.0

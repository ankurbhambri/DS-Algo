# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

'''
    Given an array of integers, and an integer N, find the length of the longest “N-stable” continuous subarray.
    An array is defined to be “N-stable” when the pair-wise difference between any two elements in the array is smaller or equal to N.
    A subarray of a 0-indexed integer array is a contiguous non-empty sequence of elements within an array.

    For instance, for array [ 4, 2, 3, 6, 2, 2, 3, 2, 7 ], and N = 1
    The return value should be 4, since the longest 1-stable subarray is [ 2, 2, 3, 2 ].
'''

from collections import deque

def func(arr, N):

    if not arr:
        return 0

    l = 0

    min_deque, max_deque = deque(), deque()

    res = 0

    for r in range(len(arr)):

        while min_deque and arr[min_deque[-1]] > arr[r]:
            min_deque.pop()
        min_deque.append(r)

        while max_deque and arr[max_deque[-1]] < arr[r]:
            max_deque.pop()
        max_deque.append(r)

        # processing
        while arr[max_deque[0]] - arr[min_deque[0]] > N:

            l += 1

            while min_deque and min_deque[0] < l:
                min_deque.popleft()

            while max_deque and max_deque[0] < l:
                max_deque.popleft()

        res = max(res, r - l + 1)

    return res

print(func([4, 2, 3, 6, 2, 2, 3, 2, 7], 1)) # 4
print(func([1, 2, 3, 4, 5], 2))  # Output: 3
print(func([1, 3, 6, 7, 8, 9], 3))  # Output: 4
print(func([10, 1, 2, 3, 4, 5], 5))  # Output: 6


# Variation

# Question: Given a string word and an integer numFriends, return the lexicographically largest string that can be formed by distributing the characters of word among numFriends friends,
# such that each friend gets at least one character.


# This is a variation of the sliding window problem where we need to find the longest substring that can be assigned to the last friend after distributing at least one character to each friend.
# The maximum length of the substring for the last friend can be calculated as max_len = total_number_of_characters - (number_of_friends - 1).
# We then iterate through the string to find the lexicographically largest substring of this maximum length.

# https://leetcode.com/problems/max-value-of-equation/description/

from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:

        q = deque()
        res = float("-inf")
        
        for j in range(len(points)):
            xj, yj = points[j]
            
            # Remove points from front where |xj - xi| > k
            while q and xj - points[q[0]][0] > k:
                q.popleft()
            
            # Compute max value using the front of deque
            if q:
                i = q[0]
                xi, yi = points[i]
                res = max(res, yi + yj + xj - xi)
            
            # Remove points from back where (yj - xj) is larger
            while q and (points[q[-1]][1] - points[q[-1]][0]) <= (yj - xj):
                q.pop()
            
            # Add current point to deque
            q.append(j)
        
        return res


print(Solution().findMaxValueOfEquation([[1,3],[2,0],[3,10],[4,5]], 1))  # Output: 4
print(Solution().findMaxValueOfEquation([[1,1],[2,2],[3,3],[4,4]], 1))  # Output: 7
print(Solution().findMaxValueOfEquation([[1,2],[2,3],[3,4],[4,5]], 1))  # Output: 6
print(Solution().findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3))  # Output: 3

# Question: Given an array of integers and a number k, find the number of contiguous subarrays of size k that contain exactly x odd numbers.


# Time Complexity: O(n)
# Space Complexity: O(1) for the variables

def count_subarrays_with_x_odds(nums, k, x):

    count = 0
    odd_count = 0
    
    for i in range(len(nums)):

        if nums[i] % 2 != 0:
            odd_count += 1
        
        if i >= k:
            if nums[i-k] % 2 != 0:
                odd_count -= 1
        
        if i >= k - 1 and odd_count == x:
            count += 1
    
    return count


print(count_subarrays_with_x_odds([1, 2, 3, 4, 5], 3, 2))  # Output: 2
print(count_subarrays_with_x_odds([1, 2, 3, 4, 5], 2, 1))  # Output: 4
print(count_subarrays_with_x_odds([1, 2, 3, 4, 5], 5, 3))  # Output: 1
print(count_subarrays_with_x_odds([1, 2, 3, 4, 5], 1, 1))  # Output: 3


# similar, but no size constraint

# Question: Given an array of integers and a number x, find the number of contiguous subarrays that contain exactly x odd numbers.

# https://leetcode.com/problems/count-number-of-nice-subarrays/


# Note: nums[r] & 1, this checks the parity of the number, where 1 means odd and 0 means even.

'''
In A[i] & 1:

    A[i] is an integer (an element of the array).
    1 has a binary representation of 000...0001 (the last bit is 1, all others are 0 in a 32-bit integer).

    This operation checks the last bit of A[i]:

        If the last bit of A[i] is 1 (which is true for odd numbers), then A[i] & 1 = 1.
        If the last bit of A[i] is 0 (which is true for even numbers), then A[i] & 1 = 0.

'''
class Solution:
    def numberOfSubarrays(self, nums, k):

        l = count = res = 0

        for r in range(len(nums)):
            if nums[r] & 1:
                k -= 1
                count = 0

            while k == 0: # here, we are counting the number of subarrays with exactly k odd numbers, while shrinking the left pointer and counting valid subarrays.
                k += nums[l] & 1
                l += 1
                count += 1

            res += count

        return res


print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))  # Output: 2
print(Solution().numberOfSubarrays([2, 4, 6], 1))  # Output: 0
print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 2))  # Output: 4
print(Solution().numberOfSubarrays([1, 2, 3, 4, 5], 1))  # Output: 5

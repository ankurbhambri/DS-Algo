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

# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums, k):

        cur = 0
        res = 0
        freq = {0: 1}

        for i in nums:

            cur += i % 2
            res += freq.get(cur - k, 0)
            freq[cur] = 1 + freq.get(cur, 0)

        return res


print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))  # Output: 2
print(Solution().numberOfSubarrays([2, 4, 6], 1))  # Output: 0
print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 2))  # Output: 4
print(Solution().numberOfSubarrays([1, 2, 3, 4, 5], 1))  # Output: 5

# https://leetcode.com/problems/maximum-alternating-subsequence-sum


# Recursion + Memoization

# TC: O(n) - Each state is computed once and there are O(n) states (index and parity).
# SC: O(n) - The recursion stack can go as deep as O(n)
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:

        memo = {}

        n = len(nums)

        def solve(idx, is_even):

            # Base case: no more elements to process
            if idx >= n:
                return 0

            # If result already calculated, return it
            if (idx, is_even) in memo:
                return memo[(idx, is_even)]

            # Option 1: Skip the current number
            skip = solve(idx + 1, is_even)

            val = nums[idx] if is_even else -nums[idx]

            # Option 2: Take the current number
            take = val + solve(idx + 1, not is_even) # invert is_even

            # Store the best result between skipping and taking
            memo[(idx, is_even)] = max(skip, take)

            return memo[(idx, is_even)]

        # Start at index 0 which is even
        return solve(0, True)


# Bottom-up DP, space optimized

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:

        even = 0  # Max sum ending at an even index

        odd = 0   # Max sum ending at an odd index

        for num in nums:

            even = max(even, odd + num) # add even element kyuki age vala element odd index ka sum hoga

            odd = max(odd, even - num) # subtract element kyuki age vala even index ka sum hoga

        return even # last me even index ka sum return karna hoga kyuki last element even index pe hoga
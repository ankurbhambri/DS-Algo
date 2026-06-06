# https://leetcode.com/problems/maximum-product-subarray

# TC: O(n)
# SC: O(1)
class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        if not nums:
            return 0

        # Shuruat pehle element se karte hain
        ans = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for i in range(1, len(nums)):

            x = nums[i]

            # Ek temporary variable chahiye kyunki current_max update hone ke baad 
            # current_min ki calculation mein purana current_max use hona chahiye.
            temp_max = max(x, current_max * x, current_min * x)
            current_min = min(x, current_max * x, current_min * x)

            current_max = temp_max

            # Final answer ko update karo
            ans = max(ans, current_max)

        return ans


print(Solution().maxProduct([-2, 0, -1]))  # Output: 0
print(Solution().maxProduct([2, 3, -2, 4]))  # Output: 6
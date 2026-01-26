# https://leetcode.com/problems/next-greater-element-iii/

# Similar to - next-permutation

class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # Step 1: Number ko digits ki list mein badle
        nums = list(str(n))
        size = len(nums)

        # Step 2: Pivot dhundein (k)
        k = -1
        for i in range(size - 2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break

        # Agar koi pivot nahi mila (number already descending hai like 321)
        if k == -1:
            return -1

        # Step 3: nums[k] se just bada digit dhundein (l)
        l = -1
        for i in range(size - 1, k, -1):
            if nums[i] > nums[k]:
                l = i
                break

        # Swap
        nums[k], nums[l] = nums[l], nums[k]

        # Step 4: Reverse right side
        nums[k+1:] = nums[k+1:][::-1]

        # Final Step: Check 32-bit limit
        res = int("".join(nums))

        # LeetCode trap check
        if res > 2147483647:
            return -1

        return res


print(Solution().nextGreaterElement(12))        # Output: 21
print(Solution().nextGreaterElement(21))        # Output: -1
print(Solution().nextGreaterElement(1234))      # Output: 1243
print(Solution().nextGreaterElement(4321))      # Output: -1
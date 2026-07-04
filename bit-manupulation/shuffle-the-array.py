# https://leetcode.com/problems/shuffle-the-array/

# TC: O(n)
# SC: O(1)
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:

        j = len(nums) - 1
        for i in range(n - 1, -1, -1):
            nums[j] <<= 10
            nums[j] |= nums[i]
            j -= 1

        i = 0
        for j in range(n, len(nums)):

            # pehle 1023 se and kardo right side ka first point ka data mil jayega
            # uske baad bacha hu data to right side shift kardo toh vo second element mil jayega
            a, b = nums[j] & 1023, nums[j] >> 10

            nums[i] = a
            nums[i + 1] = b

            i += 2

        return nums


print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))  # Output: [2, 3, 5, 4, 1, 7]
print(Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))  # Output: [1, 4, 2, 3, 3, 2, 4, 1]
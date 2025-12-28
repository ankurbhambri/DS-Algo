# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        return j + 1


print(Solution().removeDuplicates([1,1,2]))  # Output: 2
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: 5


# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)

        slow, fast = 2, 2

        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow


print(Solution().removeDuplicates([1,1,1,2,2,3]))  # Output: 5
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))  # Output: 7

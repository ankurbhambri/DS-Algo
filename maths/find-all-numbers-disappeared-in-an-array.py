# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        # Phase 1: Array ke index ko use karke present numbers ko mark karna
        for num in nums:
            idx = abs(num) - 1

            # yha pe hum array ke index ko negative kar rahe hain, jisse humein pata chalega ki kaunse numbers present hain. 
            # Agar number present hai, toh uska corresponding index negative ho jayega.
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Phase 2: Jo numbers present nahi hain, unke index ko check karna
        res = []
        for i in range(len(nums)):

            # yha pe hum check kar rahe hain ki kaunse index ke numbers positive hain, 
            # jiska matlab hai ki wo number present nahi hai.
            if nums[i] > 0:
                res.append(i + 1)

        return res


print(Solution().findDisappearedNumbers([1,1]))  # Output: [2]
print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5, 6]
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, arr):
        
        l, r = 0, len(arr) - 1
        res = 0

        while l < r:

            area = (r - l) * min(arr[l], arr[r])

            res = max(res, area)

            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1

        return res


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(Solution().maxArea([1,1]))  # 1
print(Solution().maxArea([4,3,2,1,4]))  # 16
print(Solution().maxArea([1,2,1]))  # 2
print(Solution().maxArea([1,2,4,3]))  # 4

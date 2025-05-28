# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):

        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        left_max = right_max = water = 0
        
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1
        
        return water


# print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(Solution().trap([4,2,0,3,2,5]))  # 9

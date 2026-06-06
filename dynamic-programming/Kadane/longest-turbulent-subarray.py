# https://leetcode.com/problems/longest-turbulent-subarray/

# TC: O(n)
# SC: O(1)
class Solution:
    def maxTurbulenceSize(self, arr: list[int]):

        n = len(arr)

        up = down = 1
        ans = 1

        for i in range(1, n):

            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1

            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1

            else:
                up = down = 1

            ans = max(ans, up, down)

        return ans


print(Solution().maxTurbulenceSize([4, 8, 12, 16]))  # Output: 2
print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))  # Output: 5

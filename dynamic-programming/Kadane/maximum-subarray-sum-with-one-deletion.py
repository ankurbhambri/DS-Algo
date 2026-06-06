# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/


# TC: O(n)
# SC: O(1)
class Solution:
    def maximumSum(self, arr: list[int]) -> int:

        keep = arr[0]
        delete = float('-inf')

        ans = arr[0]

        for i in range(1, len(arr)):

            nkeep = max(arr[i], keep + arr[i])

            # delete kar rhe h current element or taking the best sum till now
            ndelete = max(delete + arr[i], keep)

            keep = nkeep
            delete = ndelete

            ans = max(ans, keep, delete)

        return ans

print(Solution().maximumSum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 10
print(Solution().maximumSum([1, -2, 0, 3]))  # Output: 4
print(Solution().maximumSum([-1, -1, -1, -1]))  # Output: -1
print(Solution().maximumSum([5, 4, -1, 7, 8]))  # Output: 24
print(Solution().maximumSum([1, 2, 3, -2, 5]))  # Output: 11

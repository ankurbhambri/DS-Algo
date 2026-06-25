# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/


# TC: O(n)
# SC: O(1)
class Solution:
    def maximumSum(self, arr):

        keep = arr[0]          # no deletion
        delete = float("-inf") # one deletion used

        ans = arr[0]

        for i in range(1, len(arr)):
            
            # yha pe, ya toh new subarray start karo ya phir element to existing one mein add karo (without deletion)
            new_keep = max(arr[i], keep + arr[i])

            # Case 1 (Keep): Current element ko hi delete kar do, aur pure subarray ko keep karo
            # Case 2 (Delete): Current element ko add karo, aur pehle se hi ek deletion use kar chuke ho

            new_delete = max(
                keep,               # delete current
                delete + arr[i]     # deletion already used
            )

            keep = new_keep
            delete = new_delete

            ans = max(ans, keep, delete)

        return ans

print(Solution().maximumSum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 10
print(Solution().maximumSum([1, -2, 0, 3]))  # Output: 4
print(Solution().maximumSum([-1, -1, -1, -1]))  # Output: -1
print(Solution().maximumSum([5, 4, -1, 7, 8]))  # Output: 24
print(Solution().maximumSum([1, 2, 3, -2, 5]))  # Output: 11
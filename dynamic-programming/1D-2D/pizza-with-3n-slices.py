# https://leetcode.com/problems/pizza-with-3n-slices/


class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:

        n = len(slices)
        k = n // 3  # Humein exactly N/3 slices uthani hain

        # Helper function jo linear array ke liye max sum nikalega
        def helper(arr, k):

            memo = {}

            def dp(i, j):

                # Base Cases
                if j == 0:
                    return 0  # Saari slices chun li hain

                if i < 0:
                    return float('-inf')  # Slices khatam par target bacha hai (Invalid)

                if (i, j) in memo:
                    return memo[(i, j)]

                # Option 1: Take current slice, skip previous, pick j-1 more
                take = arr[i] + dp(i - 2, j - 1)

                # Option 2: Skip current slice, pick j from remaining
                skip = dp(i - 1, j)

                memo[(i, j)] = max(take, skip)

                return memo[(i, j)]

            return dp(len(arr) - 1, k)

        # Case 1: Pehli slice shamil hai (aakhiri excluded) -> slices[0 : n-1]
        case1 = helper(slices[:-1], k)

        # Case 2: Aakhiri slice shamil hai (pehli excluded) -> slices[1 : n]
        case2 = helper(slices[1:], k)

        return max(case1, case2)
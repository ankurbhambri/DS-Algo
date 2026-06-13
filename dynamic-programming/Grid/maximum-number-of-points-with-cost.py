# https://leetcode.com/problems/maximum-number-of-points-with-cost/


# TC: O(m * n)
# SC: O(n)
class Solution:
    def maxPoints(self, points):

        m = len(points)
        n = len(points[0])

        # Base case: Pehli row ke points se shuru karte hain
        prev_row = [points[0][j] for j in range(n)]

        # Har row ke liye process karenge (Row 1 se m-1 tak)
        for i in range(1, m):

            left = [0] * n
            right = [0] * n
            curr_row = [0] * n

            # 1. Left-to-Right Pass
            left[0] = prev_row[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, prev_row[j])

            # 2. Right-to-Left Pass
            right[n - 1] = prev_row[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, prev_row[j])

            # 3. Current Row ko Update karna
            for j in range(n):
                curr_row[j] = points[i][j] + max(left[j], right[j])

            # Agli row ke liye current row hi pichli row (prev_row) ban jayegi
            prev_row = curr_row

        # Last row ka jo bhi maximum score hoga, wahi hamara answer hai
        return max(prev_row)


print(Solution().maxPoints([[1,5],[2,3],[4,2]]))  # Output: 11
print(Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]]))  # Output: 9
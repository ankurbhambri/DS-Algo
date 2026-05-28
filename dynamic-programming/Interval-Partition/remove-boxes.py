# https://leetcode.com/problems/remove-boxes/description


# recursion + memoization
# TC: O(n^4) - 4 nested loops, SC: O(n^3) - DP table

'''
Time Complexity: O(N^4)

- Total States (N^3):
  Three variables change — l (left), r (right), and k (count of similar boxes).
  Each can go up to N, so total states = N x N x N = N^3.

- Work per State (N):
  Inside each state, a for loop runs over index m from l+1 to r,
  which can iterate up to N times.

- Total: States x Work per State = N^3 x N = O(N^4).

Note: Although the theoretical complexity is O(N^4), the while loop
and the `if boxes[m] == boxes[l]` condition prune many branches,
so it runs much faster in practice.

Space Complexity: O(N^3)

- Memoization Table (N^3):
  Every unique state (l, r, k) is stored in the memo dictionary.
  There can be at most N^3 entries.

- Recursion Stack (N):
  The recursion depth can go up to N (length of the array).

- Total: O(N^3) + O(N), dominated by O(N^3).
'''

class Solution:
    def removeBoxes(self, boxes):

        memo = {}

        def solve(l, r, count):

            if l > r:
                return 0

            # 1. Hamesha original parameters ko key banayein
            state = (l, r, count)
            if state in memo:
                return memo[state]

            # 2. Optimization: Saath wale same boxes ko count mein add karein
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                l += 1
                count += 1

            # Case 1: Is pure group (count+1 boxes) ko uda do
            res = (count + 1) * (count + 1) + solve(l + 1, r, 0)

            # Case 2: Kisi aage wale same color box 'm' ke saath merge karo
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    # Beech ke boxes (l+1 to m-1) ko saaf karo
                    # Aur m wale box ko count+1 boxes mil gaye (peeche wale)
                    res = max(res, solve(l + 1, m - 1, 0) + solve(m, r, count + 1))

            memo[state] = res # Original state store karein
            return res

        return solve(0, len(boxes) - 1, 0)


print(Solution().removeBoxes([1, 1, 1]))  # Output: 9
print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))  # Output: 23
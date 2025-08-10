# https://leetcode.com/problems/combination-sum/

# Question:
# Given an array of distinct integers `candidates` and a target integer `target`, 
# return all unique combinations of `candidates` where the chosen numbers sum to `target`.
# You may return the combinations in any order.

class Solution:
    def combinationSum(self, candidates, target: int):

        path = []

        def helper(i, curr, sm):

            if sm == target:
                path.append(curr[:])
                return

            if i >= len(candidates) or sm > target:
                return

            curr.append(candidates[i])
            helper(i, curr, sm + candidates[i])

            curr.pop()
            helper(i + 1, curr, sm)

        helper(0, [], 0)

        return path


print(Solution().combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
print(Solution().combinationSum([2, 3, 5], 8))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

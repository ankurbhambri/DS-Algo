# https://leetcode.com/problems/combination-sum/

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
print(Solution().combinationSum([1], 1))  # [[1]]
print(Solution().combinationSum([1], 2))  # [[1, 1]]
print(Solution().combinationSum([1, 2], 4))  # [[1, 1, 1, 1], [1, 1, 2], [2, 2]

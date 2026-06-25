# https://leetcode.com/problems/path-sum-iii/


class Solution:
    def pathSum(self, root, targetSum):

        # Map to store (prefix_sum: count)
        # We initialize it with {0: 1} to account for paths that 
        # sum exactly to targetSum from the root.
        prefix_sums = {0: 1}

        def dfs(node, current_sum):

            if not node:
                return 0

            # Update the prefix sum for the current node
            current_sum += node.val

            # Add current_sum to the map for child nodes to use
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

            # The number of valid paths ending at the current node is the 
            # number of times (current_sum - targetSum) has occurred before.
            count = prefix_sums.get(current_sum - targetSum, 0)

            # Recurse to children
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Backtrack: remove the current_sum from the map before returning
            prefix_sums[current_sum] -= 1

            return count

        return dfs(root, 0)
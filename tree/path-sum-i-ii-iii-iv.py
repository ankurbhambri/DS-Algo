# https://leetcode.com/problems/path-sum/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):

    def helper(node, curSum):

        if not node:
            return False

        # add the current node value to the sum
        curSum += node.val

        # if it is a leaf node means no other left or right child.
        if not node.left and not node.right:
            return curSum == targetSum

        # explore left and right nodes
        l = helper(node.left, curSum)
        r = helper(node.right, curSum)

        return l or r  # if either side is True, return True

    return helper(root, 0)


# https://leetcode.com/problems/path-sum-ii/

class Solution:
    def pathSum(self, root, target):

        res = []

        def dfs(node, path, total):

            if not node:
                return

            if(total + node.val == target and not node.left and not node.right):
                res.append(path + [node.val])
                return

            if(node.left):
                dfs(node.left, path + [node.val], total + node.val)

            if(node.right):
                dfs(node.right, path + [node.val], total + node.val)

        dfs(root, [], 0)

        return res


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


# https://leetcode.com/problems/path-sum-iv/


# Encode data

'''
nums = [113, 215, 221]

actually:

    113 → depth=1, pos=1, val=3 → root
    215 → depth=2, pos=1, val=5 → left child
    221 → depth=2, pos=2, val=1 → right child

'''
print(113//100, (113 // 100) % 10, 113 % 10)

class Solution:
    def pathSum(self, nums):
        
        # Step 1: Build map
        tree = {}

        for num in nums:
            d = num // 100
            p = (num // 10) % 10
            v = num % 10
            tree[(d, p)] = v

        # Step 2: DFS
        def dfs(d, p, curr_sum):

            if (d, p) not in tree:
                return 0

            curr_sum += tree[(d, p)]

            left = (d + 1, 2 * p - 1)
            right = (d + 1, 2 * p)

            # Leaf node
            if left not in tree and right not in tree:
                return curr_sum

            return dfs(d + 1, 2 * p - 1, curr_sum) + dfs(d + 1, 2 * p, curr_sum)
        
        return dfs(1, 1, 0)


print(Solution().pathSum([113, 221]))
print(Solution().pathSum([113, 215, 221]))
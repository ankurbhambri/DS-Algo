# https://leetcode.com/problems/range-sum-of-bst/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TC - O(N)
# SC - O(H) H - height of the tree
class Solution:
    def rangeSumBST(self, root, low, high):

        self.res = 0

        def helper(node):

            if not node:
                return 

            if low <= node.val <= high:
                self.res += node.val

            l = helper(node.left)
            r = helper(node.right)

        helper(root)
        
        return self.res


# TC - O(N)
# SC - O(H) H - height of the tree

class Solution:
    def rangeSumBST(self, root, L, R):

        q, res = [root], 0

        while q:

            node = q.pop()

            if node:
                if node.val > L:
                    q.append(node.left)    

                if node.val < R:
                    q.append(node.right)

                if L <= node.val <= R:
                    res += node.val

        return res


# Variant - 1

# Average of BST

# TC - O(N)
# SC - O(H) H - height of the tree
class Solution:
    def averageOfBST(self, root, low, high):

        self.total = 0
        self.count = 0

        def helper(node):

            if not node:
                return 

            if low <= node.val <= high:
                self.total += node.val
                self.count += 1

            l = helper(node.left)
            r = helper(node.right)

        helper(root)
        
        return self.total / self.count if self.count != 0 else 0
    

class Solution:
    def averageOfBST(self, root, L, R):

        q = [root]
        total = 0
        count = 0

        while q:

            node = q.pop()

            if node:
                if node.val > L:
                    q.append(node.left)    

                if node.val < R:
                    q.append(node.right)

                if L <= node.val <= R:
                    total += node.val
                    count += 1

        return total / count if count != 0 else 0


# Variant - 2

# What if you had to optimize your solution for 10^4 function invocations? How would our algorithm change?

# TC - O(N) for preprocessing + O(log N) per query
# SC - O(N)

class RangeSumBST:
    def __init__(self, root):

        # Step 1: Inorder traversal to collect sorted values
        self.values = []
        self._inorder(root)

        # Step 2: Build prefix sum array
        self.prefix = [0]
        for v in self.values:
            self.prefix.append(self.prefix[-1] + v)

    def _inorder(self, node):

        if not node:
            return

        self._inorder(node.left)
        self.values.append(node.val)
        self._inorder(node.right)

    # ---------- binary search implementations ----------

    def bisect_left(self, arr, target):
        """
        Returns the index of the first element >= target
        """
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def bisect_right(self, arr, target):
        """
        Returns the index of the first element > target
        """
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    # ---------- Query ----------

    def rangeSum(self, low, high):
        left_idx = self.bisect_left(self.values, low)
        right_idx = self.bisect_right(self.values, high)
        return self.prefix[right_idx] - self.prefix[left_idx]

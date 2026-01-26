# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# DFS + HashSet
class Solution:
    def findTarget(self, root, k: int) -> bool:
        seen = set()
        
        def dfs(node):
            if not node:
                return False
            
            complement = k - node.val
            if complement in seen:
                return True
            
            seen.add(node.val)
            
            # Left ya Right kahin bhi mil jaye toh True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

# Inorder + Two Pointers
class Solution:
    def findTarget(self, root, k: int) -> bool:

        nums = []
        
        def inorder(node):

            if not node:
                return
            
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # similar to 2 sum problem in sorted array
        left, right = 0, len(nums) - 1
        
        while left < right:

            current_sum = nums[left] + nums[right]

            if current_sum == k:
                return True

            elif current_sum < k:
                left += 1

            else:
                right -= 1
        
        return False


# Iterative Two-Pointer

'''
Concept: The "BST Iterator"

    Left Iterator: Yeh humein BST ka sabse chota element dega (Inorder: Left -> Root -> Right).

    Right Iterator: Yeh humein BST ka sabse bada element dega (Reverse Inorder: Right -> Root -> Left).

'''

# Similar to Kth Smallest Element in a BST and Binary Search Tree Iterator

# TC: O(N)
# SC: O(H), H tree is height
class Solution:
    def findTarget(self, root, k: int) -> bool:

        if not root:
            return False

        # Do stacks pointers ko track karne ke liye
        left_stack = []
        right_stack = []

        # Left pointer ko sabse chote element par le jao
        curr_l = root
        while curr_l:
            left_stack.append(curr_l)
            curr_l = curr_l.left

        # Right pointer ko sabse bade element par le jao
        curr_r = root
        while curr_r:
            right_stack.append(curr_r)
            curr_r = curr_r.right

        # Pointers ko move karna start karo
        while left_stack and right_stack:

            left_node = left_stack[-1]
            right_node = right_stack[-1]

            # Agar dono same node par hain, toh kaam khatam
            if left_node == right_node:
                break

            current_sum = left_node.val + right_node.val

            if current_sum == k:
                return True

            elif current_sum < k:
                # Sum chota hai, left pointer ko next bade element par le jao
                node = left_stack.pop()
                curr = node.right
                while curr:
                    left_stack.append(curr)
                    curr = curr.left
            else:
                # Sum bada hai, right pointer ko next chote element par le jao
                node = right_stack.pop()
                curr = node.left
                while curr:
                    right_stack.append(curr)
                    curr = curr.right

        return False
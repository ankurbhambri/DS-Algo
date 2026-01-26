'''
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.
Example 2:

Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4
Example 3:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7
 

Constraints:

    The depth of the n-ary tree is less than or equal to 1000.
    The total number of nodes is between [1, 10^4].
'''

from backtracking.combinations import Solution


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = 0

        def dfs(node):

            nonlocal ans

            if node is None:
                return 0
            
            m1 = 0  # First maximum depth
            m2 = 0  # Second maximum depth

            for child in node.children:

                depth = dfs(child)

                if depth > m1:
                    m2 = m1
                    m1 = depth

                elif depth > m2:
                    m2 = depth
            
            ans = max(ans, m1 + m2)

            return m1 + 1

        dfs(root)
        return ans

print(Solution().diameter(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))  # Output: 3
# print(Solution().diameter(Node(1, [Node(2), Node(3, [Node(6), Node(7)]), Node(4), Node(5)])))  # Output: 3
print(Solution().diameter(Node(1, [Node(2), Node(3, [Node(6), Node(7)]), Node(4), Node(5)])))  # Output: 4
# https://leetcode.com/problems/nested-list-weight-sum/description/

from typing import List, Union

from collections import deque

'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

    Input: [[1,1],2,[1,1]]
    Output: 10 
    Explanation: Four 1's at depth 2, one 2 at depth 1.
    Example 2:

    Input: [1,[4,[6]]]
    Output: 27 
    Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

'''

# TC: O(n)
# SC: O(d) where d is the maximum depth of the nested list

def depthSum(nestedList, depth=1):

    if not nestedList:
        return 0

    total = 0

    for elem in nestedList:

        if isinstance(elem, int):
            total += elem * depth

        else:
            total += depthSum(elem, depth + 1)

    return total


print(depthSum([[1, 1], 2, [1, 1]]))  # Output: 10
print(depthSum([1, [4, [6]]]))  # Output: 27
print(depthSum([1, [2, [3, [4, 5]], 6], 7]))  # Output: 69


# Variant 1: Define Schema for NestedInteger

class Object:
    def __init__(self):
        self.value: List[Union['Object', int]]


class Solution:
    def depthSum(self, nestedList: List[Object]) -> int:

        def dfs(nlist, depth = 1):

            total = 0

            for item in nlist:

                if isinstance(item, int):
                    total += item * depth

                else:
                    total += dfs(item.value, depth + 1)

            return total

        return dfs(nestedList)


obj1 = Object()
obj1.value = [1, 1]
obj2 = Object()
obj2.value = [1, 1]
obj_main = [obj1, 2, obj2]

sol = Solution()
print(sol.depthSum(obj_main))  # Output: 10

obj_inner = Object()
obj_inner.value = [6]
obj_mid = Object()
obj_mid.value = [4, obj_inner]
obj_main2 = [1, obj_mid]

print(sol.depthSum(obj_main2))  # Output: 27


# Schema + BFS Approach
class Solution:
    def depthSum(self, nestedList: List['Object']) -> int:
       
        q = deque(nestedList)

        level = 1

        sm = 0

        while q:

            for _ in range(len(q)):

                item = q.popleft()

                if isinstance(item, int):
                    sm += item * level

                else:
                    q.extend(item.value)

            level += 1

        return sm

obj1 = Object()
obj1.value = [1, 1]
obj2 = Object()
obj2.value = [1, 1]
obj_main = [obj1, 2, obj2]

sol = Solution()
print(sol.depthSum(obj_main))  # Output: 10

obj_inner = Object()
obj_inner.value = [6]
obj_mid = Object()
obj_mid.value = [4, obj_inner]
obj_main2 = [1, obj_mid]

print(sol.depthSum(obj_main2))  # Output: 27

# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst

# Pascal triangle is used to calculate the number of ways to reorder the array to get the same BST. The number of ways to reorder the array is equal to the number of ways to choose the left and right subtrees from the remaining elements after choosing the root.

# Here, we need to make sure the relative order of the left and right subtrees is maintained. So, we can use the formula:

# C(n, k) = n! / (k! * (n - k)!)

# where n is the total number of elements in the left and right subtrees, and k is the number of elements in the left subtree.


class Solution:
    def numOfWays(self, nums: list[int]) -> int:

        n = len(nums)

        MOD = 10 ** 9 + 7

        # Pascal Triangle
        PT = []
        for i in range(1, n + 1):
            if i == 1:
                PT.append([1])
            else:
                old = [0] + PT[-1] + [0]
                cur = []
                for j in range(len(old) - 1):
                    cur.append((old[j] + old[j + 1]))
                PT.append(cur)

        def dfs(nums):

            m = len(nums)

            if m < 3: 
                return 1

            # elements less than the root will be in the left subtree
            left_nodes = [a for a in nums if a < nums[0]]

            # elements greater than the root will be in the right subtree
            right_nodes = [a for a in nums if a > nums[0]]

            # why this formula? C(n, k) = n! / (k! * (n - k)!)

            # we need this formular because we have first position fixed for the root then we left with N -1 places total

            # elements that needs to be in left subtree with do N -1 places C left nodes

            # simularly for right subtree we have N -1 places C right nodes

            # but here left and right value will come same from factorial formula so we can just do C(N -1, left nodes) or C(N -1, right nodes) both will give same result

            # so will do C(N -1, left nodes) and then multiply with the result of left and right subtree

            return dfs(left_nodes) * dfs(right_nodes) * PT[m - 1][len(left_nodes)] % MOD

        return (dfs(nums) - 1) % MOD

print(Solution().numOfWays([2, 1, 3]))  # 1
print(Solution().numOfWays([3, 4, 5, 1, 2]))  # 5
print(Solution().numOfWays([1, 2, 3]))  # 0

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
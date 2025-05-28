# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012

# Top down (Memoization)


def frogJump(n: int, heights) -> int:

    memo = [-1] * n

    def helper(i):

        if i == 0:
            return 0

        if memo[i] != -1:
            return memo[i]

        left = helper(i - 1) + abs(heights[i] - heights[i - 1])

        right = (
            helper(i - 2) + abs(heights[i] - heights[i - 2]) if i > 1 else float("inf")
        )

        memo[i] = min(left, right)

        return memo[i]

    return helper(n - 1)


# Bottom up (Tabulation)
def frogJump(n: int, heights) -> int:

    dp = [0] * n
    for i in range(1, n):
        left = dp[i - 1] + abs(heights[i] - heights[i - 1])
        right = dp[i - 2] + abs(heights[i] - heights[i - 2]) if i > 1 else float("inf")
        dp[i] = min(left, right)
    return dp[n - 1]


# Space optimized way
def frogJump(n: int, heights) -> int:

    a = b = 0
    for i in range(1, n):
        left = b + abs(heights[i] - heights[i - 1])
        right = a + abs(heights[i] - heights[i - 2]) if i > 1 else float("inf")
        a, b = b, min(left, right)
    return b



# https://leetcode.com/problems/frog-jump/description/

from collections import deque

class Solution:
    def canCross(self, stones):

        n = len(stones)
        if stones[1] != 1:  # Pehla jump 1 unit ka hona chahiye
            return False
        
        # Set to quickly check if a position is a stone
        stone_set = set(stones)
        
        # BFS: (current position, previous jump size)
        queue = deque([(1, 1)])  # Start at stones[1] with jump size 1
        visited = {(1, 1)}  # (position, jump_size)
        
        while queue:
            curr_pos, prev_jump = queue.popleft()
            
            if curr_pos == stones[-1]:  # Last stone reached
                return True
            
            # Try jumps: k-1, k, k+1
            for jump in [prev_jump - 1, prev_jump, prev_jump + 1]:
                if jump > 0:  # Jump size should be positive
                    next_pos = curr_pos + jump
                    if next_pos in stone_set and (next_pos, jump) not in visited:
                        queue.append((next_pos, jump))
                        visited.add((next_pos, jump))
        
        return False

print(Solution().canCross([0,1,3,5,6,8,12,17]))  # Output: True
print(Solution().canCross([0,1,2,3,4,8,9,11]))  # Output: False

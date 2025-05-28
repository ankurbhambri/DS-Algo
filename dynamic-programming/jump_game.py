# https://leetcode.com/problems/jump-game/
# TC: O(n)

# Greedy + DP

from collections import deque

class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:  # Agar current index max_reach se aage hai, stuck!
                return False
            max_reach = max(max_reach, i + nums[i])  # Update max reachable index
            if max_reach >= len(nums) - 1:  # Agar last index tak pahunch gaye
                return True
        return True


print(Solution().canJump([2, 3, 1, 1, 4]))  # True
print(Solution().canJump([3, 2, 1, 0, 4]))  # False

# https://leetcode.com/problems/jump-game-ii/
# TC: O(n)

class Solution:
    def jump(self, nums):

        jumps = 0
        curr_end = 0
        next_end = 0

        for i in range(len(nums) - 1):  # stop before the last index
            next_end = max(next_end, i + nums[i])

            if i == curr_end:
                jumps += 1
                curr_end = next_end
                if curr_end >= len(nums) - 1:  # Last, reached
                    break

        return jumps

print(Solution().jump([2, 3, 1, 1, 4]))  # 2
print(Solution().jump([2, 3, 0, 1, 4]))  # 2


# https://leetcode.com/problems/jump-game-iii/description/
# O(n2)

def canReach(arr, start):
    q = deque()
    q.append(start)
    visited = set()
    
    while q:
        idx = q.popleft()
        
        if arr[idx] == 0:
            return True
        
        for x in ((idx + arr[idx]), (idx - arr[idx])):
            
            if 0 <= x < len(arr) and x not in visited:
                q.append(x)
                visited.add(idx) 
    return False


print(canReach([4,2,3,0,3,1,2], 5)) # True
print(canReach([4,2,3,0,3,1,2], 0))  # True


# https://leetcode.com/problems/jump-game-vii/description/

from collections import deque

def canReach(s: str, minJump: int, maxJump: int) -> bool:

    n = len(s)
    queue = deque([0])  # Start from index 0
    farthest = 0        # Track the farthest index we've explored

    while queue:
        i = queue.popleft()

        # Start exploring from the max of previously explored to i + minJump
        start = max(i + minJump, farthest + 1)
        end = min(i + maxJump, n - 1)

        for j in range(start, end + 1):
            if s[j] == '0':
                if j == n - 1:
                    return True
                queue.append(j)

        # Update the farthest we've checked so far
        farthest = end

    return False


print(canReach("011010", 2, 3))  # True
print(canReach("01101110", 2, 3))  # False


# printing the path
def jump_path(nums):

    res = 0
    l = r = 0
    path = []

    while r < len(nums) - 1:
        far = 0
        next_index = -1

        for i in range(l, r + 1):
            if i + nums[i] > far:
                far = i + nums[i]
                next_index = i

        l = r + 1
        r = far
        path.append(next_index)
        res += 1

    path.append(len(nums) - 1)
    return res, path

print(jump_path([3, 3, 0, 2, 1, 2, 4, 2, 0, 0]))
print(jump_path([2, 3, 1, 1, 4]))
print(jump_path([2, 3, 0, 1, 4]))

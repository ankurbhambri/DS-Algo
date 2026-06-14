from collections import deque, defaultdict


# https://leetcode.com/problems/jump-game/

# TC: O(n)
# Greedy + DP
class Solution:
    def canJump(self, nums: list[int]) -> bool:

        max_reachable = 0

        for i in range(len(nums)):

            # Agar current index tak hum pahunch hi nahi sakte
            if i > max_reachable:
                return False

            # Max reachable distance ko update karo
            max_reachable = max(max_reachable, i + nums[i])

        return True


print(Solution().canJump([2, 3, 1, 1, 4]))  # True
print(Solution().canJump([3, 2, 1, 0, 4]))  # False


# https://leetcode.com/problems/jump-game-ii/

# TC: O(n)
# SC: O(1)

# Here, we have gurantee that path exists, but we need to find in how many jumps we can reach the end?
class Solution:
    def jump(self, nums: list[int]) -> int:

        end = 0
        jumps = 0
        farthest = 0

        for i in range(len(nums) - 1):

            # yha guranteed h ki n - 1 tak phuch jaoge, nhi yoh humme jump 1 ki tarah check karna padte i > farthest.
            farthest = max(farthest, i + nums[i])

            # yha mein fathest end nikal ke check karta hu beech ke sabhi farthest, and jump += 1 karta rahega
            # isse kya hoga ki end ko chase karte i new farthest nikal lega
            # and ek time ayega ki hum end ka farthest nikal chukenge honge
            if i == end:
                jumps += 1
                end = farthest

        return jumps


print(Solution().jump([2, 3, 1, 1, 4]))  # 2
print(Solution().jump([2, 3, 0, 1, 4]))  # 2


# https://leetcode.com/problems/jump-game-iii/description/

# TC: O(n)
# SC: O(n)

# Here we are using using BFS to explore all reachable indices from the start index, till then the index where arr[idx] == 0.
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:

        n = len(arr)
        q = deque([start])
        visited = {start}

        while q:

            i = q.popleft()

            if arr[i] == 0:
                return True

            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return False


print(Solution().canReach([4,2,3,0,3,1,2], 5)) # True
print(Solution().canReach([4,2,3,0,3,1,2], 0))  # True


# https://leetcode.com/problems/jump-game-iv/description/

# TC: O(n)
# SC: O(n)

# Find the minimum steps to reach to the end, that's why using BFS.
class Solution:
    def minJumps(self, arr: list[int]) -> int:

        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            for _ in range(len(q)):

                i = q.popleft()

                if i == n - 1:
                    return steps

                neighbors = graph[arr[i]]
                neighbors.append(i - 1)
                neighbors.append(i + 1)

                for nxt in neighbors:
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

                # ek bar process kar liya toh future mein dobara kabhi bhi ye list use karne ki zarurat nahi.
                graph[arr[i]].clear()

            steps += 1

        return -1


print(Solution().minJumps([7,7,2,1,7,7,7,3,4,1]))  # 3


# https://leetcode.com/problems/jump-game-v/


# TC: O(n * d) in worst case, but often much better due to early breaks
# SC: O(n) for the dp array and recursion stack

# Yha d ka matlab h ki hum maximum d steps jump kar sakte hain ek building se dusri building pe.
class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:

        n = len(arr)

        # memo array subproblems ka answer store karne ke liye
        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]

            best = 1 # Khud us index ko count karke minimum 1 toh hoga hi

            # 1. Right side mein jumps check karna
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break # Rasta block ho gaya, aage nahi ja sakte
                best = max(best, 1 + dfs(j))

            # 2. Left side mein jumps check karna
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break # Rasta block ho gaya
                best = max(best, 1 + dfs(j))

            memo[i] = best

            return best

        # Kyunki hum kisi bhi index se shuru kar sakte hain, 
        # isliye sabhi index se check karke maximum nikalenge.
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))

        return ans


# https://leetcode.com/problems/jump-game-vi/description/

from collections import deque

# TC: O(n)
# SC: O(n) for the dp array and Monotonic decreasing deque
class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:

        n = len(nums)

        # dp[i] store karega index i tak pahonchne ka max score
        dp = [0] * n
        dp[0] = nums[0]

        # Deque mein hum indices store karenge
        dq = deque([0])

        for i in range(1, n):

            # 1. Jo indices k step se zyada piche chale gaye, unhe aage se nikal do
            if dq[0] < i - k:
                dq.popleft()

            # 2. Deque ke aage hamesha max value hogi, toh dp[i] nikal lo
            dp[i] = nums[i] + dp[dq[0]]

            # 3. Monotonic property maintain karo: 
            # Agar naya dp[i] piche wali chhoti values se bada hai, toh unhe hata do
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            # 4. Current index ko push karo
            dq.append(i)

        return dp[-1]


# https://leetcode.com/problems/jump-game-vii/description/

# TC: O(n)
# SC: O(n)
def canReach(s: str, minJump: int, maxJump: int) -> bool:

    n = len(s)
    farthest = 0        # Track the farthest index we've explored
    queue = deque([0])  # Start from index 0

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


# https://leetcode.com/problems/jump-game-viii/description/


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

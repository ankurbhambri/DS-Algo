# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/description/

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # Agar rectangle pehle se square hai, toh 1 hi answer hoga
        if n == m:
            return 1
            
        # Grid banayein jo track karegi kaunsa cell bhar gaya hai
        grid = [[False] * m for _ in range(n)]
        self.ans = n * m  # Worst case: saare 1x1 ke squares

        def is_valid(r, c, k):
            """Check karta hai kya (r,c) par k size ka square fit ho sakta hai"""
            if r + k > n or c + k > m:
                return False
            for i in range(r, r + k):
                for j in range(c, c + k):
                    if grid[i][j]:
                        return False
            return True

        def cover(r, c, k, val):
            """Square ko grid par lagane ya hatane ke liye"""
            for i in range(r, r + k):
                for j in range(c, c + k):
                    grid[i][j] = val

        def dfs(count):
            # Pruning: Agar current count pehle hi best ans se bada ho gaya toh ruk jao
            if count >= self.ans:
                return

            # 1. Pehla khali cell dhoondo (Top-to-Bottom, Left-to-Right)
            r, c = -1, -1
            for i in range(n):
                for j in range(m):
                    if not grid[i][j]:
                        r, c = i, j
                        break
                if r != -1:
                    break

            # Agar koi khali cell nahi mila, matlab rectangle bhar gaya!
            if r == -1:
                self.ans = min(self.ans, count)
                return

            # 2. Bada se bada square size dhoondo jo yahan fit ho sake
            max_k = min(n - r, m - c)
            
            # 3. Bade se chote size ke squares try karein (Greedy approach fast karti hai)
            for k in range(max_k, 0, -1):
                if is_valid(r, c, k):
                    # Square lagao
                    cover(r, c, k, True)
                    # Agle khali cell par jao
                    dfs(count + 1)
                    # Backtrack: Square hatao
                    cover(r, c, k, False)

        dfs(0)
        return self.ans
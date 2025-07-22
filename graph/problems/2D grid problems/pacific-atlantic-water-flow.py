# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

# Idea: Here the logic is to start from the boundaries of the Pacific and Atlantic oceans and perform a DFS to find all cells that can flow into these oceans.
# The cells that can flow into both oceans will be the intersection of the visited cells from both DFS traversals.
# Time Complexity: O(R * C) where R is the number of rows and C is the number of columns in the grid.
# Space Complexity: O(R * C) for the visited sets.

class Solution:
    def pacificAtlantic(self, heights):

        # pac = pacific, atl = atlantic
        pac, atl = [], []

        R, C = len(heights), len(heights[0])

        # visit_pac = visited pacific, visit_atl = visited atlantic
        visit_pac, visit_atl = set(), set()
        
        # Pacific Boundaries
        for r in range(R):
            pac.append((r, 0))
            atl.append((r, C - 1))
            
        # Atlantic Boundaries
        for c in range(C):
            pac.append((0, c))
            atl.append((R - 1, c))
            
        # All four directions
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c, visit):

            visit.add((r, c))

            for dr, dc in dirs:

                x, y = r + dr, c + dc

                if (0 <= x < R and 0 <= y < C and heights[r][c] <= heights[x][y] and (x, y) not in visit):
                    dfs(x, y, visit)

        for r, c in pac:
            dfs(r, c, visit_pac)
            
        for r, c in atl:
            dfs(r, c, visit_atl)

        # Similar coordinates in visit_atl and visit_pac so that water can flow.
        return list(visit_atl & visit_pac)


print(Solution.pacificAtlantic([[2,1],[1,2]]))  # Output: [[0,0],[0,1],[1,0],[1,1]]
print(Solution.pacificAtlantic([[1,1],[1,1],[1,1]]))  # Output: [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
print(Solution.pacificAtlantic([[1,2,3],[8,9,4],[7,6,5]]))  # Output: [[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]
print(Solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))  # Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

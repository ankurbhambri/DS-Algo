from collections import deque
from heapq import heappop, heappush

'''
Problems solved using Multi-source BFS:

- Walls and Gates
- Closest DashMart
- Nearest Exit from Entrance in Maze
- Nearest Hospital
- Nearest Police Station
- 01 Matrix
- Rotting Oranges
- Escape the Spreading Fire
'''

# https://leetcode.com/problems/walls-and-gates/

# INF means that the room is empty and needs to be filled with the distance to the nearest gate.

# TC: O(m*n)
# SC: O(m*n)
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:

        if not rooms:
            return

        queue = deque()
        rows, cols = len(rooms), len(rooms[0])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:  # Gate found
                    queue.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        while queue:

            r, c = queue.popleft()

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))


print(Solution().wallsAndGates(
    [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
)) # output: [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]



'''
Closest DashMart

A DashMart is a warehouse run by DoorDash that houses items found in convenience stores, grocery stores, and restaurants. 
We have a city with open roads, blocked-off roads, and DashMarts.

City planners want you to identify how far a location is from its closest DashMart.

You can only travel over open roads (up, down, left, right).

Locations are given in [row, col] format.

Example 1
[
    ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X'] 
]

' ' represents an open road that you can travel over in any direction (up, down, left, or right).
'X' represents an blocked road that you cannot travel through.
'D' represents a DashMart.

list of pairs [row, col]

locations = [
    [200, 200],
    [1, 4],
    [0, 3],
    [5, 8],
    [1, 8],
    [5, 5]
]

answer = [-1, 2, 0, -1, 6, 9]

Provided:
    - city: char[][]
    - locations: int[][2]
    - Return: answer: int[]

Return a list of the distances from a given point to its closest DashMart.

'''

# TC: O(m*n)
# SC: O(m*n)
def closest_dashmart(city, locations):

    queue = deque()

    rows, cols = len(city), len(city[0]) if city else 0

    dist = [[-1] * cols for _ in range(rows)]  # Distance to closest DashMart

    # Step 1: Add all DashMart positions to the queue
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == 'D':
                dist[r][c] = 0
                queue.append((r, c))

    # Step 2: Multi-source BFS
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    # Output: [-1, 2, 0, -1, 6, 9]
    while queue:

        r, c = queue.popleft()

        for dr, dc in directions:

            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:

                if city[nr][nc] != 'X':
                    queue.append((nr, nc))

                dist[nr][nc] = dist[r][c] + 1

    # Step 3: Answer queries
    answer = []
    for r, c in locations:

        if 0 <= r and r < rows and 0 <= c and c < cols:
            answer.append(dist[r][c])

        else:
            answer.append(-1)
    
    return answer


print(closest_dashmart([
    ['X', ' ', ' ', 'D', ' ', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
    [' ', ' ', ' ', 'D', 'X', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'D', ' ', 'X', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X'],
    [' ', ' ', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
], [
    [200, 200],
    [1, 4],
    [0, 3],
    [5, 8],     
    [1, 8],
    [5, 5]
]))  # Output: [-1, 2, 0, -1, 6, 9]

print(closest_dashmart([
    ['X', 'X'],
    ['X', 'D'],
], [
    [0, 1],
    [1, 0],
    [1, 1]
]))  # Output: [1, 1, 0]


# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/


# Same as DashMart

# TC: O(m*n)
# SC: O(m*n)
class Solution:
    def nearestExit(self, maze, entrance):

        row, col = len(maze), len(maze[0])

        dist = [[-1] * col for _ in range(row)]

        q = deque()

        # left/right boundary to put the exits in the queue
        for r in range(row):

            if maze[r][0] == "." and [r, 0] != entrance:
                if dist[r][0] == -1:
                    dist[r][0] = 0
                    q.append((r, 0))

            if maze[r][col - 1] == "." and [r, col - 1] != entrance:
                if dist[r][col - 1] == -1:
                    dist[r][col - 1] = 0
                    q.append((r, col - 1))

        # top/bottom boundary to put the exits in the queue
        for c in range(col):

            if maze[0][c] == "." and [0, c] != entrance:
                if dist[0][c] == -1:
                    dist[0][c] = 0
                    q.append((0, c))

            if maze[row - 1][c] == "." and [row - 1, c] != entrance:
                if dist[row - 1][c] == -1:
                    dist[row - 1][c] = 0
                    q.append((row - 1, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # BFS on the exists towards the entrance.
        while q:

            r, c = q.popleft()

            if [r, c] == entrance:
                return dist[r][c]

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < row and
                    0 <= nc < col and
                    maze[nr][nc] == "." and
                    dist[nr][nc] == -1
                ):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return -1



'''

Nearest Hospital

There are N cities. Cities are connected by roads, (Basically given a graph). 

K of the cities has a hospital(Given an array of size K). 

Time taken to reach a hospital from a city is no of edges to the nearest city which contains a hospital. 

Find the maximum time taken to reach a hospital from all the N cities.
'''

# TC: O(n + e)
# SC: O(n)
def max_time_to_hospital(n, edges, hospitals):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * n
    q = deque()

    for h in hospitals:
        dist[h] = 0
        q.append(h)

    while q:

        node = q.popleft()

        for nei in graph[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                q.append(nei)

    return max(dist)

print(max_time_to_hospital(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [0]))  # Output: 4
print(max_time_to_hospital(6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], [3, 5]))  # Output: 3


'''
Nearest Police Station

There is a grid with police stations, 1 thief, and 1 bank. Every police station can patrol within k Manhattan distance. 

You need to determine if there is any path for the thief to reach the bank without encountering the police.

'''

# TC: O(m*n)
# SC: O(m*n)
def can_reach_bank(grid, k):
    rows = len(grid)
    cols = len(grid[0])

    police = []
    thief = bank = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'P':
                police.append((r, c))
            elif grid[r][c] == 'T':
                thief = (r, c)
            elif grid[r][c] == 'B':
                bank = (r, c)

    # --------------------
    # Phase 1: Mark unsafe cells
    # --------------------
    unsafe = [[False] * cols for _ in range(rows)]

    q = deque()

    for r, c in police:
        q.append((r, c, 0))
        unsafe[r][c] = True

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        r, c, dist = q.popleft()

        if dist == k:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and not unsafe[nr][nc]:
                unsafe[nr][nc] = True
                q.append((nr, nc, dist + 1))

    # thief or bank already covered
    if unsafe[thief[0]][thief[1]]:
        return False

    if unsafe[bank[0]][bank[1]]:
        return False

    # --------------------
    # Phase 2: BFS from thief
    # --------------------
    q = deque([thief])
    visited = {thief}

    while q:
        r, c = q.popleft()

        if (r, c) == bank:
            return True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                not unsafe[nr][nc] and
                (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                q.append((nr, nc))

    return False


print(can_reach_bank([
    [' ', ' ', ' ', 'P', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'T', ' ', ' ', ' ', 'B'],
], 1))  # Output: True

print(can_reach_bank([
    [' ', ' ', ' ', 'P', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'T', ' ', ' ', ' ', 'B'],
], 2))  # Output: False



# https://leetcode.com/problems/01-matrix/description/

# TC: O(m*n)
# SC: O(m*n)
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        rows, cols = len(mat), len(mat[0])

        q = deque([])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            r, c = q.popleft()

            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                nr, nc = r + x, c + y

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat


# https://leetcode.com/problems/escape-the-spreading-fire


# TC: O(m*n log(m*n)) because of the Dijkstra's algorithm part
# SC: O(m*n)

# Steps to solve this problem

# Pehle, humme nikalna h ki fire har cell tak kitne time mein pahuchti hai. Iske liye hum multi-source BFS karenge starting from all the fire cells.

# Uske baad hum binary search lga ke check karenge ki itna time/delay wait karne ke baad kya hum fire se bach ke destination tak pahuch sakte hain.

# Iske liye hum BFS karenge starting from (0, 0) aur check karenge ki kya hum destination tak pahuch sakte hain without stepping into a cell jahan fire already pahuch chuki hai.
class Solution:
    def maximumMinutes(self, grid: list[list[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # fire arrival time
        fire = [[float('inf')] * cols for _ in range(rows)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fire[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] != 2
                    and fire[nr][nc] == float('inf')
                ):
                    fire[nr][nc] = fire[r][c] + 1
                    q.append((nr, nc))

        def can_escape(wait):

            # fire reaches start before or at waiting time
            if wait >= fire[0][0]:
                return False

            q = deque([(0, 0, wait)])
            visited = {(0, 0)}

            while q:

                r, c, t = q.popleft()

                if (r, c) == (rows - 1, cols - 1):
                    return True

                for dr, dc in dirs:

                    nr, nc = r + dr, c + dc
                    time = t + 1

                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == 2 or (nr, nc) in visited:
                        continue

                    # destination special case
                    if (nr, nc) == (rows - 1, cols - 1):

                        if time <= fire[nr][nc]:
                            visited.add((nr, nc))
                            q.append((nr, nc, time))

                    else:

                        if time < fire[nr][nc]:
                            visited.add((nr, nc))
                            q.append((nr, nc, time))

            return False

        lo, hi = 0, 10**9

        ans = -1

        while lo <= hi:

            mid = (lo + hi) // 2

            if can_escape(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans


# https://leetcode.com/problems/find-the-safest-path-in-a-grid/


# Steps to solve this problem:

# Phle hum multi-source BFS karenge starting from all the thief cells to find the distance of each cell from the nearest thief.

# Uske baad hum Dijkstra's algorithm lga ke find karenge maximum safeness factor path from (0, 0) to (R-1, C-1). Yaha pe hum minimum distance to thief ko check karenge, kyunki hume maximum safeness chahiye.
class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1:
            return 0

        R, C = len(grid), len(grid[0])
        thief_dist = [[float("inf")] * C for _ in range(R)]

        thief = deque()

        for i in range(R * C):
            if grid[i // C][i % C] == 1:
                thief.append((i // C, i % C))
                thief_dist[i // C][i % C] = 0
        
        # Multi-source BFS to find the distance of each cell from the nearest thief
        while thief:

            r, c = thief.popleft()

            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                a, b = r + x, c + y

                if 0 <= a < R and 0 <= b < C and thief_dist[a][b] == float("inf"):

                    thief_dist[a][b] = thief_dist[r][c] + 1

                    thief.append((a, b))


        # Dijikstra's algorithm to find the maximum safeness factor path from (0, 0) to (R-1, C-1)
        visit = {}

        q = [(-thief_dist[0][0], 0, 0)]

        while q:

            safety, r, c = heappop(q)

            safety = -safety # to make positive, kyunki hume maximum safeness chahiye

            if (r, c) == (R - 1, C - 1):
                return safety

            if (r, c) in visit or visit[(r, c)] >= safety:
                continue

            visit[(r, c)] = safety

            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                a, b = r + x, c + y

                if 0 <= a < R and 0 <= b < C and (a, b) not in visit:

                    # yha pe minimum distance to thief ko check karna hoga, kyunki hume maximum safeness chahiye
                    new_dist = min(safety, thief_dist[a][b])

                    heappush(q, (-new_dist, a, b))

        return -1


print(Solution().maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]])) # 2
print(Solution().maximumSafenessFactor([[0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])) # 1
# https://cses.fi/problemset/task/1194/

import sys
from collections import deque

# here idea is to do multi source bfs for monsters first to get their reach time to each cell
# then do bfs for player ensuring that player only goes to cells which he can reach before monsters
# if player reaches boundary, we reconstruct path using parent array

def solve():
    # Input handling
    input_data = sys.stdin.read().split()
    if not input_data: return
    n, m = int(input_data[0]), int(input_data[1])
    grid = input_data[2:]

    monster_dist = [[float('inf')] * m for _ in range(n)]
    player_dist = [[float('inf')] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]
    
    mq = deque()
    pq = deque()
    start_node = None

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'M':
                mq.append((r, c))
                monster_dist[r][c] = 0
            elif grid[r][c] == 'A':
                start_node = (r, c)
                player_dist[r][c] = 0

    # 1. Multi-source BFS for Monsters
    directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
    while mq:
        r, c = mq.popleft()
        for dr, dc, _ in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#' and monster_dist[nr][nc] == float('inf'):
                monster_dist[nr][nc] = monster_dist[r][c] + 1
                mq.append((nr, nc))

    # 2. BFS for Player
    pq.append(start_node)
    
    # Boundary check for starting position
    if start_node[0] == 0 or start_node[0] == n-1 or start_node[1] == 0 or start_node[1] == m-1:
        print("YES")
        print(0)
        print("")
        return

    while pq:
        r, c = pq.popleft()
        
        for dr, dc, move in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.' and player_dist[nr][nc] == float('inf'):
                new_dist = player_dist[r][c] + 1
                # Must reach before any monster
                if new_dist < monster_dist[nr][nc]:
                    player_dist[nr][nc] = new_dist
                    parent[nr][nc] = (r, c, move)
                    pq.append((nr, nc))
                    
                    # Check if reached boundary
                    if nr == 0 or nr == n-1 or nc == 0 or nc == m-1:
                        # Path reconstruction
                        path = []
                        curr_r, curr_c = nr, nc
                        while (curr_r, curr_c) != start_node:
                            pr, pc, move = parent[curr_r][curr_c]
                            path.append(move)
                            curr_r, curr_c = pr, pc
                        
                        print("YES")
                        print(len(path))
                        print("".join(path[::-1]))
                        return

    print("NO")

solve()
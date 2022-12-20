  # Walls and Gates leetcode problem
  
  def walls_and_gates(self, rooms):
      r, c = len(rooms), len(rooms[0])
      q = deque()
      visit = set()

      for i in range(r): # starting with gates and filling rest of rooms with shortest distance
          for j in range(c):
              if rooms[i][j] == 0:
                  q.append([i, j])
                  visit.add((i, j))

      def helper(x, y): # checking whether things are out of bounce or not wall etc
          if x < 0 or x == r or y < 0 or y == c or rooms[x][y] == -1 or (x, y) in visit:
              return
          q.append([x, y])
          visit.add((x, y))

      depth = 0
      while q:
          for i in range(len(q)): # layer by layer
              a, b = q.popleft()
              rooms[a][b] = depth # changing in rooms array
              # all four directions checking 
              helper(a + 1, b)
              helper(a - 1, b)
              helper(a, b + 1)
              helper(a, b - 1)

          depth += 1 # once done incremet the depth of queue

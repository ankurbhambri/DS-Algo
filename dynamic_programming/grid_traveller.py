dp = {}
def grid_traveller(m, n):

  if (m, n) in dp:
    return dp[(m, n)]
  elif m == 1 and n == 1:
    return 1
  elif m == 0 or n == 0:
    return 0

  dp[(m, n)] = grid_traveller(m - 1, n) + grid_traveller(m, n - 1)
  
  return dp[(m, n)]

print(grid_traveller(4, 3))
print(grid_traveller(2, 2))
print(grid_traveller(500, 500))
  

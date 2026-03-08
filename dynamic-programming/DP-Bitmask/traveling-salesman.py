def solve_tsp_bitmask(dist_matrix):

    memo = {} # Memoization table: (mask, last_city) -> min_distance
    n = len(dist_matrix)

    # Represent 'all cities visited' (e.g., for 4 cities, 1111 in binary is 15)
    final_mask = (1 << n) - 1

    def dp(mask, pos):

        # Base Case: If all cities are visited, return distance back to start (city 0)
        if mask == final_mask:
            return dist_matrix[pos][0]

        # Check if we've already solved this state
        state = (mask, pos)
        if state in memo:
            return memo[state]

        res = float('inf')

        # Try visiting every city we haven't visited yet
        for next_city in range(n):
            # Check if the next_city bit is NOT set in the mask
            if not (mask & (1 << next_city)):
                # Update mask and recurse
                new_dist = dist_matrix[pos][next_city] + dp(mask | (1 << next_city), next_city)
                res = min(res, new_dist)

        memo[state] = res
        return res

    # Start at city 0, with only city 0 in the mask (1 << 0 = 1)
    return dp(1, 0)


matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(f"The shortest path distance is: {solve_tsp_bitmask(matrix)}")
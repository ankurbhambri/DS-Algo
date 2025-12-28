# https://www.codechef.com/problems/CATS


def func(n, parent, jump):

    LOG = 18  # Maximum bits for binary lifting

    # Mark which nodes are occupied
    occupied = [False] * (n + 1)  # Using 1-based index

    # Initialize dp array for binary lifting (LOG x n+1)
    dp = [[-1] * (n + 1) for _ in range(LOG)]

    # Fill dp[0] with the parent array values (adjusted for 1-based index)
    for i in range(1, n + 1):
        dp[0][i] = parent[i - 1]

    # Build binary lifting table
    for i in range(1, LOG):
        for j in range(1, n + 1):
            if dp[i - 1][j] != -1:
                dp[i][j] = dp[i - 1][dp[i - 1][j]]

    # Function to calculate the number of jumps for a given node
    def calc(node):

        curr = jump[node - 1]  # Adjusting for 1-based index

        if occupied[curr]:
            return 0  # Already occupied

        j = 1  # Initialize jump count
        for i in range(LOG - 1, -1, -1):  # Traverse binary lifting table
            jp = dp[i][curr]
            if jp != -1 and not occupied[jp]:
                curr = jp
                j += 1 << i  # Add the number of jumps for this bit

        # Mark the final node as occupied
        occupied[curr] = True
        return j

    # Store results for each node and return them
    result = []
    for i in range(1, n + 1):
        result.append(calc(i))

    return result


# Example call to the function with test input
print(func(7, [2, 4, 0, 3, 3, 3, 4], [7, 6, 2, 1, 4, 5, 3]))

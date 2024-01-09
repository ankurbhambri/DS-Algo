def digitSum(n):
    # Function to calculate digit sum
    return sum(int(d) for d in str(n))


def canVisit(row, col, k):
    # Check if the cell can be visited based on the digit sum condition
    return digitSum(row) + digitSum(col) <= k


def movingCount(graph, k):
    m, n = len(graph), len(graph[0])

    visited = set()
    queue = [(0, 0)]
    count = 0

    # Perform BFS traversal
    while queue:
        row, col = queue.pop(0)
        if (
            (0 <= row < m)
            and (0 <= col < n)
            and canVisit(row, col, k)
            and (row, col) not in visited
        ):
            visited.add((row, col))
            count += 1

            queue.append((row + 1, col))
            queue.append((row - 1, col))
            queue.append((row, col + 1))
            queue.append((row, col - 1))

    return count


# Example usage:
k = 18
graph = [[0, 0, 1], [18, 1, 1], [0, 18, 0]]
result = movingCount(graph, k)
print("Number of cells the robot can reach:", result)

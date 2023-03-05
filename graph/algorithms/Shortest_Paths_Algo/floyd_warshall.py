'''
Floyd-Warshall algorithm | All pairs shortest path - Dynamic Programming - o(n^3)
'''


def floyd_warshall(n, graph):

    temp = graph  # copy
    for k in range(n):
        for i in range(n):
            for j in range(n):
                temp[i][j] = min(temp[i][j], temp[i][k] + temp[k][j])
    return graph


graph = [
    [0, 3, float("inf"), 7],
    [8, 0, 2, float("inf")],
    [5, float("inf"), 0, 1],
    [2, float("inf"), float("inf"), 0],
]
print(floyd_warshall(4, graph))

'''Shortest path algorithm works with negative weights but when the cycle found it fials
It runs algorithm V - 1 times relations of vertices using edges weights - o(n^2)'''


def bellman_ford(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(k + 1):

        temp = prices.copy()
        for s, d, p in flights:

            if prices[s] == float("-inf"):
                continue

            if prices[s] + p < temp[d]:
                temp[d] = prices[s] + p

        prices = temp

    return -1 if prices[dst] == float("inf") else prices[dst]


# n is nos of edges, flights is adjacency list, src as source, dst as destination with k stops

print(
    bellman_ford(
        n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1
    )
)

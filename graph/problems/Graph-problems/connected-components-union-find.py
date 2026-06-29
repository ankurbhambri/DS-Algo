def solution(n, edges):

    rank = [1] * n

    par = [i for i in range(n)]

    def find(node):
        if node != par[node]:
            par[node] = find(par[node])
        return par[node]

    def union(node1, node2):

        p1 = find(node1)
        p2 = find(node2)

        # If both nodes parent are same then union is not possible
        if p1 == p2:
            return 0  # Same parent

        if rank[p1] < rank[p2]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        return 1

    res = n  # Here, the logic subtracts the total nodes by the number of unions, which returns 1 if the union is successfull

    # subrtacting the number of unions from the total nodes will give us the number of connected components
    # because each union reduces the number of connected components by 1
    # for example, if we have 5 nodes and we perform 2 unions, we will have 3 connected components left
    # in case of a complete graph, the number of connected components will be 1, because all nodes are connected to each other
    for n1, n2 in edges:
        res -= union(n1, n2)

    return res


print(solution(5, [[0, 1], [1, 2], [3, 4]])) # Output: 2
print(solution(5, [[0, 1], [1, 2], [2, 3], [3, 4]])) # Output: 1


# similar - https://leetcode.com/problems/minimum-time-for-k-connected-components/
# https://leetcode.com/problems/minimize-maximum-component-cost/
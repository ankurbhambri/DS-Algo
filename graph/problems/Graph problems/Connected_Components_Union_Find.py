def solution(n, edges):
    par = [i for i in range(n)]
    rank = [1] * n

    def find(node):
        if node != par[node]:
            par[node] = find(par[node])
        return par[node]

    def union(node1, node2):
        p1 = find(node1)
        p2 = find(node2)

        # If both nodes parent are same then union is not possible
        if p1 == p2:
            return 0 # Same parent

        if rank[p1] < rank[p2]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        return 1
        
    res = n # Here, the logic subtracts the total nodes by the number of unions, which returns 1 if the union is successful
    for n1, n2 in edges:
        res -= union(n1, n2)

    return res
    
print(solution(5, [[0,1], [1,2], [3,4]]))
        

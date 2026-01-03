'''

Given tree graph with N nodes/regions (1 to N) and (N - 1) bidirectional edges/roads.
Each node/region (i + 1) has no. of towns denoted by towns[i].

Calculate min difference in total sum of towns between resulting components when you delete one edge.

int minTownsDiff(int N, vector<int>& towns, vector<vector<int>>& roads)

Input:
2
10 20
1 2

Output: 10

Constraints:
1 <= N <= 10^5
1 <= towns[i] <= 10^4

'''

def minTownsDiff(N, towns, roads):

    adj = [[] for _ in range(N)]
    for u, v in roads:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    total_sum = sum(towns)
    # min_diff ko global ya non-local rakhna padega DFS ke liye
    self_min_diff = float('inf')

    def dfs(u, p):

        nonlocal self_min_diff
        current_sum = towns[u]
        
        for v in adj[u]:
            if v != p:
                child_sum = dfs(v, u)
                current_sum += child_sum
        
        # Is node ke subtree ko alag karne par diff kya hoga?
        # abs(total_sum - 2 * current_sum) means -> (total_sum - current_sum) - current_sum
        # here, (total_sum - current_sum) is the sum of the other component
        diff = abs(total_sum - 2 * current_sum)
        self_min_diff = min(self_min_diff, diff)

        return current_sum

    dfs(0, -1)
    return self_min_diff


print(minTownsDiff(5, [4, 2, 1, 6, 3], [[1, 2], [1, 3], [3, 4], [3, 5]]))
print(minTownsDiff(2, [10, 20], [[1, 2]]))
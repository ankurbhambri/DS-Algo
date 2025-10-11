# https://algo.monster/liteproblems/256

'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
The cost of  painting each house with a certain color is different. You have to  paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on.

Find the minimum cost to paint all houses.

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.

'''

def solution(costs):

    n, m = len(costs), len(costs[0])

    for i in range(1, n):

        for j in range(m):

            a = costs[i - 1][j - 1] if j > 0 else float("inf")
            b = costs[i - 1][j + 1] if j + 1 < m else float("inf")

            costs[i][j] = costs[i][j] + min(a, b)

    return min(costs[-1])

print(solution([[17, 2, 17],[16, 16, 5],[14, 3, 19]]))

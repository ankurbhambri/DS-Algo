# https://leetcode.com/problems/climbing-stairs/

# 70. Climbing Stairs

# This forms a recurrence relation: ways(n) = ways(n - 1) + ways(n - 2)


def climbStairs(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


print(climbStairs(2))  # 2
print(climbStairs(3))  # 3
print(climbStairs(4))  # 5


# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
def minCostClimbingStairs(cost):
    n = len(cost)
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[n - 1], cost[n - 2])


print(minCostClimbingStairs([10, 15, 20]))  # 15

# https://leetcode.com/problems/climbing-stairs/

# 70. Climbing Stairs


def climbStairs(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


print(climbStairs(2))  # 2
print(climbStairs(3))  # 3
print(climbStairs(4))  # 5


# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

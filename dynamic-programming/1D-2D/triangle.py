# https://leetcode.com/problems/triangle/submissions/


# (top-down approach)
# TC = O(N * N)
# SC = O(1)
def triangle_top_down(triangle):
    n = len(triangle)
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i - 1]):
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] = (
                    min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
                )

    return min(triangle[-1])


print(triangle_top_down([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))


# (bottom-up approach)
# TC = O(N * N)
# SC = O(1)
def triangle_bottom_up(triangle):
    n = len(triangle)
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = (
                min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
            )
    return triangle[0][0]


print(triangle_bottom_up([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))

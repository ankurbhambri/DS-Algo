# https://leetcode.com/problems/flood-fill/


# TC: O(N) where N is the number of pixels in the image
# SC: O(N) in worst case when all pixels are of the same color and we
class Solution:
    def floodFill(self, image, sr, sc, color):

        row, col = len(image), len(image[0])

        cur_color = image[sr][sc]

        def dfs(sr, sc):

            if (
                sr < 0
                or sr >= row
                or sc < 0
                or sc >= col
                or image[sr][sc] != cur_color
                or image[sr][sc] == color
            ):
                return

            image[sr][sc] = color

            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)

        dfs(sr, sc)
        return image


print(Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))  # [[0, 0, 0], [0, 1, 1]]
print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))  # [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
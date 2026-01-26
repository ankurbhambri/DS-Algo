# https://leetcode.com/problems/separate-squares-i/

class Solution:
    def separateSquares(self, squares):

        max_y, total_area = 0, 0

        for x, y, l in squares:
            total_area += l ** 2
            max_y = max(max_y, y + l)

        def check(limit_y):

            area = 0

            for x, y, l in squares:

                top_y = y + l
                bot_y = y

                if limit_y > top_y:
                    area += l * l

                elif limit_y > bot_y:
                    area += l * (limit_y - y)

            return area >= total_area / 2

        lo, hi = 0, max_y
        eps = 1e-5
        res = 0.0
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            res = mid
            if check(mid):
                hi = mid
            else:
                lo = mid

        return res
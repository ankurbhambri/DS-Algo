# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i


# sabse pehle hum points ko set mein dalange taki O(1) mein check kar sakein ki koi point exist karta hai ya nahi
# fir hum har pair of points ke liye check karenge ki kya ye dono points rectangle ke opposite corners ho sakte hain. Agar haan, 
# toh hum check karenge ki kya rectangle ke andar koi aur point hai ya nahi. Agar nahi hai, toh hum area calculate karenge aur maximum area ko update karenge.

# TC: O(N^2 * M) where N is number of points and M is number of points inside the rectangle (in worst case, M can be N)
# SC: O(N) for storing points in set
class Solution:
    def maxRectangleArea(self, points: list[list[int]]) -> int:
        n = len(points)

        point_set = set((x, y) for x, y in points)

        ans = -1

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # Rectangle ban hi nahi sakta
                if x1 == x2 or y1 == y2:
                    continue

                # Dusre 2 corners hone chahiye
                if (x1, y2) not in point_set or (x2, y1) not in point_set:
                    continue

                left = min(x1, x2)
                right = max(x1, x2)
                bottom = min(y1, y2)
                top = max(y1, y2)

                valid = True

                for x, y in points:

                    # agar koi point rectangle ke andar hai
                    # and vo point rectangle ke corners mein se nahi hai, toh rectangle valid nahi hai
                    # kyu ki hum chahte hain ki rectangle ke andar koi aur point na ho, sirf corners hi allowed hain
                    if left <= x <= right and bottom <= y <= top:

                        corner = (
                            (x, y) == (x1, y1) or
                            (x, y) == (x2, y2) or
                            (x, y) == (x1, y2) or # diagonal corner
                            (x, y) == (x2, y1)    # diagonal corner
                        )

                        if not corner:
                            valid = False
                            break

                if valid: # agar koi point rectangle ke andar nahi hai, toh area calculate karo
                    # width = right - left
                    # height = top - bottom
                    area = (right - left) * (top - bottom)
                    ans = max(ans, area)

        return ans
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

    def query_range(self, l, r):
        if l > r:
            return 0
        return self.query(r) - self.query(l - 1)


# TC: O(N log N) for sorting and O(N log M) for Fenwick Tree operations, where N is the number of points and M is the number of unique Y-coordinates
# SC: O(N + M) for storing points and Fenwick Tree
class Solution:
    def maxRectangleArea(self, xCoord: list[int], yCoord: list[int]) -> int:

        n = len(xCoord)

        # Step 1: Coordinate Compression for Y-coordinates
        # Kyunki Y ki values 8 * 10^7 tak hain, hum unhe 1 se M tak ranks de denge
        unique_ys = sorted(list(set(yCoord)))
        y_to_rank = {y: rank for rank, y in enumerate(unique_ys, 1)}

        # Step 2: Points ko X-coordinate ke basis par group karna
        col_points = {}
        for i in range(n):

            x = xCoord[i]
            y = yCoord[i]

            if x not in col_points:
                col_points[x] = []

            col_points[x].append(y)

        # Har column ke andar Y-coordinates ko sort karna aur pooray columns ko X ke hisab se sort karna
        sorted_x = sorted(col_points.keys())

        for x in sorted_x:
            col_points[x].sort()

        max_area = -1

        # last_seen track karega ki koi specific Y-pair pichli baar kis X par dikha tha
        # key: (y1, y2), value: (prev_x, points_count_at_that_time)
        last_seen = {}

        # Fenwick tree initialize karenge total unique Ys ke size se
        bit = FenwickTree(len(unique_ys))

        # Step 3: Sweep-Line from Left to Right (Sorted X ke hisab se)
        for x in sorted_x:

            ys = col_points[x]
            m = len(ys)

            # Pehle check karenge ki kya is column ke adjacent pairs se koi valid rectangle ban raha hai
            for i in range(m - 1):

                y1 = ys[i]
                y2 = ys[i + 1]

                if (y1, y2) in last_seen:

                    prev_x, prev_total_points = last_seen[(y1, y2)]

                    r1 = y_to_rank[y1]
                    r2 = y_to_rank[y2]

                    # Fenwick Tree se check karenge ki y1 se y2 ke beech mein total kitne points hain abhi tak
                    current_total_points = bit.query_range(r1, r2)

                    # Agar pichli baar se lekar ab tak is Y-range mein koi naya point NAHI aaya hai,
                    # toh points_inside_or_on_border 0 hoga (yaani rectangle bilkul khali hai)
                    points_inside_or_on_border = current_total_points - prev_total_points

                    if points_inside_or_on_border == 0:

                        current_area = (x - prev_x) * (y2 - y1)

                        max_area = max(max_area, current_area)

            # Ab is current column ke saare points ko Fenwick Tree mein update/insert karenge
            for y in ys:
                bit.update(y_to_rank[y], 1)

            # Is current column ke saare pairs ke liye last_seen ko update karenge
            for i in range(m - 1):

                y1 = ys[i]
                y2 = ys[i + 1]

                r1 = y_to_rank[y1]
                r2 = y_to_rank[y2]

                # Hum save kar rahe hain current X aur current time par is range mein total points ka count
                last_seen[(y1, y2)] = (x, bit.query_range(r1, r2))

        return max_area


print(Solution().maxRectangleArea([1, 1, 3, 3], [1, 3, 1, 3]))  # Output: 4
print(Solution().maxRectangleArea([1, 1, 3, 3, 2], [1, 3, 1, 3, 2]))  # Output: -1
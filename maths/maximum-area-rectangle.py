class Solution:
    def maxAreaRect(self, points: list[list[int]]) -> int:
        
        n = len(points)

        # 1. Shuru mein hi saare points ko set mein daal do
        visit = set((x, y) for x, y in points)

        res = 0  # Max area track karne ke liye (0 se shuru kar sakte hain)

        # 2. Har do points ka pair check karo
        for i in range(n):

            x1, y1 = points[i]

            for j in range(i + 1, n): # i + 1 se start karne par duplicate pairs check nahi honge

                x2, y2 = points[j]

                # 3. Valid diagonal condition: x aur y dono alag hone chahiye
                if x1 != x2 and y1 != y2:
                    # 4. Check karo kya counter-diagonal points set mein hain toh rectangle ban sakta hai
                    if (x1, y2) in visit and (x2, y1) in visit:
                        size = abs(x2 - x1) * abs(y2 - y1)
                        res = max(res, size)

        return res if res != 0 else 0  # Agar koi rectangle nahi bana, toh 0 return karo


print(Solution().maxAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))  # Output: 4
print(Solution().maxAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))  # Output: 2
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import heapq


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:

        # 1. Sabhi workers ka (ratio, quality) nikal kar ratio ke hisab se sort kar lo
        # ratio = wage / quality
        workers = []
        for q, w in zip(quality, wage):
            workers.append((w / q, q))

        workers.sort() # Ratio ke ascending order mein sort ho gaya

        max_heap = []
        total_quality = 0
        min_cost = float('inf') # Shuruat mein cost ko infinity maan liya

        # 2. Ek-ek karke har worker par iterate karo
        for ratio, q in workers:

            # Current worker ki quality ko total mein add karo aur heap mein daalo
            total_quality += q

            # Python mein default min-heap hota hai, isliye max-heap banane ke liye '-' sign lagaya hai
            heapq.heappush(max_heap, -q)

            # Agar heap mein k se zyada workers ho gaye hain, toh sabse bade quality wale ko nikal do
            if len(max_heap) > k:
                # Kyunki humne negative daala tha, heappop karne par sabse badi quality (jo sabse choti negative hogi) bahar aayegi
                biggest_q = -heapq.heappop(max_heap)
                total_quality -= biggest_q

            # 3. Jaise hi hamare paas barabar K workers ho jayein, cost calculate karo
            if len(max_heap) == k:
                current_cost = ratio * total_quality
                min_cost = min(min_cost, current_cost) # Sabse minimum cost ko track karo

        return min_cost


print(Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))  # Output: 105.00000
print(Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3))  # Output: 30.66667
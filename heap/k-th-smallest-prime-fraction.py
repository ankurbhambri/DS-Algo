# https://leetcode.com/problems/k-th-smallest-prime-fraction/


import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):

        # Sabse chote fractions ko track karne ke liye ek min-heap (pq) banaya
        pq = []

        # Array ki total length nikal li
        N = len(arr)

        # 1. Shuruat mein, har ek element ko sabse bade element (arr[N-1]) se divide karke
        # jo sabse chote possible fractions banenge, unhe heap mein daal rahe hain.
        # Format: (fraction_value, numerator_index, denominator_index)
        for i in range(N):
            heapq.heappush(pq, ((arr[i] / arr[N - 1]), i, N - 1))

        # 2. Hame k-th sabse chota element chahiye.
        # Isliye hum (k - 1) baar loop chalayenge aur sabse chote elements ko nikalte jayenge.
        for _ in range(k - 1):

            # Heap ke top se sabse chota fraction bahar nikala
            cur = heapq.heappop(pq)

            # Ab isi numerator (n) ke liye agla bada fraction dhoondhne ke liye
            # denominator ka index ek kadam peeche (d = cur[2] - 1) le jayenge
            n, d = cur[1], cur[2] - 1

            # Kahani tabhi aage badhegi jab tak numerator ka index, denominator ke index se chota ho
            # (kyunki fraction < 1 hona chahiye, aur array sorted hai)
            if d > n:
                # Agla possible fraction heap mein daal diya
                heapq.heappush(pq, ((arr[n] / arr[d]), n, d))

        # 3. (k - 1) elements nikalne ke baad, ab heap ke top par jo baitha hai,
        # vahi hamara k-th sabse chota fraction hai.
        result = heapq.heappop(pq)

        # result[1] se numerator ka original number aur result[2] se denominator ka original number le kar return kar diya
        return [arr[result[1]], arr[result[2]]]


print(Solution().kthSmallestPrimeFraction([1, 7], 1))  # [1, 7]
print(Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3))  # [2, 5]
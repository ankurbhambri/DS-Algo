# https://leetcode.com/problems/longest-happy-string/

import heapq


class Solution:
    def longestDiverseString(a, b, c):
        # Max-heap of (-count, char) to always get the character with the most remaining count
        res, max_heap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        while max_heap:
            # Get the character with the highest remaining count
            first_count, first_char = heapq.heappop(max_heap)
            if len(res) >= 2 and res[-1] == res[-2] == first_char:
                if not max_heap:
                    break
                # If the first character would form "aaa", "bbb", or "ccc", take the second highest
                second_count, second_char = heapq.heappop(max_heap)
                res += second_char
                second_count += 1  # decrement count (negative value)
                if second_count:
                    heapq.heappush(max_heap, (second_count, second_char))
                heapq.heappush(max_heap, (first_count, first_char))
            else:
                res += first_char
                first_count += 1  # decrement count (negative value)
                if first_count:
                    heapq.heappush(max_heap, (first_count, first_char))

        return res


print(Solution.longestDiverseString(1, 1, 7))  # "ccaccbcc"
print(Solution.longestDiverseString(2, 2, 1))  # "ababc"
print(Solution.longestDiverseString(0, 0, 5))  # "ababc"

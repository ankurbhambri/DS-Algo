'''
    The problem involved a list of airports with flight arrival and departure times.
'''

from collections import defaultdict
from heapq import heappush, heappop
from math import inf


class Solution:
    def earliestArrival(self, flights, src, dst):

        graph = defaultdict(list)

        for u, v, depart, arrive in flights:
            graph[u].append((v, depart, arrive))

        pq = [(0, src)]  # (arrival_time, airport)

        best = defaultdict(lambda: inf)
        best[src] = 0

        while pq:

            cur_time, airport = heappop(pq)

            if airport == dst:
                return cur_time

            if cur_time > best[airport]:
                continue

            for nxt, depart, arrive in graph[airport]:

                if depart >= cur_time and arrive < best[nxt]:

                    best[nxt] = arrive
                    heappush(pq, (arrive, nxt))

        return -1
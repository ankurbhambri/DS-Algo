# https://medium.com/the-1-hour-dsa-prep-room/google-l4-onsite-question-flight-connection-planner-39578db37a0d

import heapq
from collections import defaultdict

class Flight:
    def __init__(self, src, dest, dep, arr):
        self.src = src
        self.dest = dest
        self.dep = dep
        self.arr = arr


def get_min_wait_time(flights: list[Flight], start: str, end: str) -> int:

    graph = defaultdict(list)
    for f in flights:
        graph[f.src].append(f)

    # (wait, time, city)
    pq = [(0, 0, start)]

    best = defaultdict(lambda: float('inf'))

    # (city, arrival_time) -> min_wait_time
    best[(start, 0)] = 0

    while pq:

        parent_wait_time, arrival_time, cur_city = heapq.heappop(pq)

        # Agar destination mil gaya, toh yahi humara minimum wait time hai
        if cur_city == end:
            return parent_wait_time

        # Agar is state par hum pehle isse behtar (kam wait time mein) aa chuke hain, toh skip karein
        if best[(cur_city, arrival_time)] < parent_wait_time:
            continue

        # Next flights explore karna
        for next_flight in graph[cur_city]:

            # Condition: Agli flight ka departure current arrival ke baad hona chahiye
            if next_flight.dep >= arrival_time:

                # Edge Case: Agar start city hai, toh koi wait time nahi (ghar se aaye hain)
                child_wait_time = 0 if cur_city == start else (next_flight.dep - arrival_time)

                new_total_wait = parent_wait_time + child_wait_time

                # Agar is nayi state par pehle se kam wait time mil raha hai, toh PQ mein daalein
                state_key = (next_flight.dest, next_flight.arr)
                if new_total_wait < best[state_key]:

                    # source is from where we came and dest is where we need to go
                    state_key = (next_flight.dest, next_flight.arr)

                    best[state_key] = new_total_wait

                    heapq.heappush(pq, (new_total_wait, next_flight.arr, next_flight.dest))

    return -1  # Agar destination tak pahunchne ka koi raasta nahi hai


flight_list = [
    Flight("A", "B", 1, 10),
    Flight("A", "B", 2, 6),
    Flight("A", "B", 3, 4),
    Flight("B", "C", 5, 8),
    Flight("B", "D", 7, 9),
    Flight("C", "D", 9, 12)
]

start_city = "A"
end_city = "D"

result = get_min_wait_time(flight_list, start_city, end_city)
print(f"Minimum Waiting Time from {start_city} to {end_city} is: {result}")


# https://codeforces.com/blog/entry/142476

'''
Given an origin airport, destination airport, and series of flights determine whether it is possible for a package at the origin to reach the destination. 

A flight is represented as departure airport, arrival airport, departure time, and arrival time. 

During the transportation, the time that the package leaves the airport needs to be greater than or equal to the time it arrives at the airport. 

Please determine whether it is possible for a package transfer from s to t. The package arrived at s at time 0.

E.g. 1
Origin: "NYC"
Destination: "SFO"
Flights: {{NYC -> LAX, Departure: 0, Arrival: 4}, {LAX -> SFO, Departure: 5, Arrival: 7}}
Output: True

E.g 2
Origin: "NYC"
Destination: "SFO"
Flights:{{NYC -> LAX, Departure: 0, Arrival: 4}, {LAX -> SFO, Departure: 3, Arrival: 5}}
Output: False
'''


class Flight:
    def __init__(self, src, dest, dep, arr):
        self.src = src
        self.dest = dest
        self.dep = dep
        self.arr = arr

class Solution:
    def can_package_reach_destination(self, flights: list[Flight], start: str, end: str) -> bool:

        graph = defaultdict(list)
        for f in flights:
            graph[f.src].append(f)

        pq = []

        # (time, city)
        heapq.heappush(pq, (0, start))

        # (city, arrival_time) -> visited
        visited = set()
        visited.add((start, 0))

        while pq:

            arrival_time, cur_city = heapq.heappop(pq)

            if cur_city == end:
                return True

            for next_flight in graph[cur_city]:

                if next_flight.dep >= arrival_time:

                    state_key = (next_flight.dest, next_flight.arr)

                    if state_key not in visited:
                        visited.add(state_key)
                        heapq.heappush(pq, (next_flight.arr, next_flight.dest))

        return False


print(Solution().can_package_reach_destination(
    [Flight("NYC", "LAX", 0, 4), Flight("LAX", "SFO", 5, 7)],
    "NYC",
    "SFO"
))  # True

print(Solution().can_package_reach_destination(
    [Flight("NYC", "LAX", 0, 4), Flight("LAX", "SFO", 3, 5)],
    "NYC",
    "SFO"
))  # False
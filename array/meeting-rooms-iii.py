# https://leetcode.com/problems/meeting-rooms-iii/description/

import heapq

class Solution:
    def mostBooked(self, n, meetings):

        # Sort meetings by start time
        meetings.sort(key=lambda x: x[0])

        # Min heap of available rooms by number
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        # Min heap of busy rooms: (end_time, room_number)
        busy_rooms = []

        # Meeting count per room
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that have ended before this meeting
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room_id = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_id)

            if available_rooms:
                room_id = heapq.heappop(available_rooms)
                count[room_id] += 1
                # Meeting runs normally
                heapq.heappush(busy_rooms, (end, room_id))
            else:
                # Must wait for earliest free room
                earliest_end, room_id = heapq.heappop(busy_rooms)
                count[room_id] += 1
                # Meeting duration remains same
                duration = end - start
                new_end = earliest_end + duration
                heapq.heappush(busy_rooms, (new_end, room_id))

        # Find room with max meetings
        ans = 0
        for i in range(1, n):
            if count[i] > count[ans]:
                ans = i
        return ans

print(Solution().mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))  # Output: 0
print(Solution().mostBooked(3, [[1,20],[2,10],[3,5],[4,9]]))  # Output: 2
print(Solution().mostBooked(4, [[1,3],[2,4],[3,5],[4,6]]))  # Output: 0
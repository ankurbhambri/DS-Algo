# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:
    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:

        if self.overlapping(start, end):
            self.booking.append([start, end])
            return True

        return False

    def overlapping(self, start, end):

        for s, e in self.booking:
            if start < e and end > s:
                return False
        return True


obj = MyCalendar()
print(obj.book(10, 20))  # True
print(obj.book(20, 21))  # True
print(obj.book(20, 25))  # False


# https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:
    def __init__(self):
        self.bookings = []   # all events
        self.overlaps = []   # double booked intervals

    def book(self, start: int, end: int) -> bool:

        # Step 1: check triple booking
        for s, e in self.overlaps:
            if start < e and end > s:
                return False   # triple booking detected

        # Step 2: find new overlaps with existing bookings
        for s, e in self.bookings:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))

        # Step 3: add booking
        self.bookings.append((start, end))
        return True


# https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree:
    def __init__(self):
        self.delta = {}

    def book(self, start: int, end: int) -> int:
        
        # mark start and end
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end]   = self.delta.get(end, 0) - 1
        
        # sweep to compute max overlap
        ans = 0
        ongoing = 0
        
        for t in sorted(self.delta):
            ongoing += self.delta[t]
            ans = max(ans, ongoing)

        return ans


# similar problems:

# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips, capacity):

        delta = []

        for p, u, v in trips:
            delta.append((u, p))
            delta.append((v, -p))

        for _, p in sorted(delta):
            capacity -= p
            if capacity < 0:
                return False

        return True

# https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings, n):

        hm = [0] * (n + 1)

        for i, j, v in bookings:
            hm[i - 1] += v
            hm[j] -= v

        for i in range(1, n):
            hm[i] += hm[i - 1]

        return hm[:-1]


print(Solution().corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))  # [10,55,45,25,25]
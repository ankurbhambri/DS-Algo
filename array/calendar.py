from sortedcontainers import SortedDict

# https://leetcode.com/problems/my-calendar-i/


class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:

        if self.overlapping(start, end):
            self.booking.append([start, end])
            return True

        return False

    def overlapping(self, s, e):

        for a, b in self.booking:
            if (s >= a and s < b) or (e > a and e <= b) or (a > s and b < e):
                return False
        return True


obj = MyCalendar()
print(obj.book(10, 20))  # True
print(obj.book(20, 21))  # True
print(obj.book(20, 25))  # False


# https://leetcode.com/problems/my-calendar-ii/


class MyCalendarTwo:

    def __init__(self):
        self.booking = []
        self.overlap = []

    def book(self, s: int, e: int) -> bool:

        for a, b in self.overlap:
            if max(s, a) < min(e, b):
                return False

        for i, j in self.booking:
            if max(s, i) < min(e, j):
                self.overlap.append([max(s, i), min(e, j)])

        self.booking.append([s, e])
        return True


class MyCalendarTwo:

    def __init__(self):
        self.booking_count = SortedDict()
        self.max_overlapped_booking = 2

    def book(self, start: int, end: int) -> bool:

        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlapped_booking = 0
        print(self.booking_count)
        # Calculate the prefix sum of bookings.
        for count in self.booking_count.values():
            overlapped_booking += count

            if overlapped_booking > self.max_overlapped_booking:
                # Rollback changes.
                self.booking_count[start] -= 1
                self.booking_count[end] += 1

                return False

        return True


# https://leetcode.com/problems/my-calendar-iii/submissions/


class MyCalendarThree:

    def __init__(self):
        self.booking_count = SortedDict()
        self.max_overlapped_booking = 2

    def book(self, start: int, end: int) -> bool:

        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlapped_booking = 0
        res = 0
        for count in self.booking_count.values():

            overlapped_booking += count

            res = max(res, overlapped_booking)

        return res


# similar problems:
# https://leetcode.com/problems/car-pooling/
# https://leetcode.com/problems/corporate-flight-bookings/submissions/

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
        pass

    def book(self, start: int, end: int) -> bool:
        pass

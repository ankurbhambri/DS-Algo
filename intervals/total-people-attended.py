"""
The bookstore hosted a set of meetings across 24 hours.

Question #3: Given a list of meetings with the hours they started and ended at (as 
  numbers from 1 to 24), and the size of their audience, return the largest total number
  of people that attended meetings simultaneously, across a continuous period of time.

Example: [
    Meeting(title = "The Age of Fiction",   audience = 10, start = 1, end = 4),
    Meeting(title = "Audiobook Publishing", audience = 20, start = 3, end = 8),
    Meeting(title = "National Novel Month", audience = 30, start = 5, end = 8),
]
Result: 50
Explanation: The largest number of people attended between 5:00 and 8:00, 
  when the last two meetings were taking place at the same time.
"""

class Meeting:  # This is an object that represents a meeting
    def __init__(self, title: str, audience: int, start: int, end: int):
        self.title = title
        self.audience = audience
        self.start = start
        self.end = end


def largest_number_of_people(meetings):

    meets = [0] * 25
    for m in meetings:
        meets[m.start] += m.audience
        # if m.end < 24:
        meets[m.end] -= m.audience

    res = 0
    curr_res = 0

    for i in range(25):
        curr_res += meets[i]
        res = max(res, curr_res)

    return res


input_1 = [
    Meeting(title="The Age of Fiction", audience=10, start=1, end=4),
    Meeting(title="Audiobook Publishing", audience=20, start=3, end=8),
    Meeting(title="National Novel Month", audience=30, start=5, end=8),
]
assert largest_number_of_people(input_1) == 50

input_2 = [
    Meeting(title="Publishing with Kickstarter", audience=18, start=1, end=5),
    Meeting(title="History of Paranormal Stories", audience=2, start=20, end=24),
    Meeting(title="30 Authors Under 30", audience=30, start=8, end=15),
    Meeting(title="Writing Circle", audience=12, start=12, end=16),
    Meeting(title="Photography for Cookbooks", audience=5, start=13, end=22),
]
assert largest_number_of_people(input_2) == 47


input_3 = [
    Meeting(title="Publishing with Kickstarter", audience=18, start=1, end=5),
    Meeting(title="History of Paranormal Stories", audience=2, start=20, end=24),
]
assert largest_number_of_people(input_3) == 18

print("Passed")

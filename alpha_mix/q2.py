# https://leetcode.com/discuss/interview-question/6058077/Google-or-L4-or-On-site-or-Bangalore

"""

I was being asked this question today on On-Site Round 2 for L4 position of Google Software Engineer. Tried applying basic scheduling algorithm to schedule the meetings and exclude the part where it is 'Do Not Schedule'.

Although I missed covering a few edge cases. Couldn't think of any other solution. Any other alternative solutions?

You have a list of meetings in your calendar with a start and end time.
You are very busy, so meetings can overlap.
You also have one "Do Not Schedule" interval during which you don't attend any meeting.
Any meeting schedule that overlaps with a DNS slot is automatically cut such that it does not overlap with the DNS slot anymore.


Return a list of non-overlapping time intervals when you are in a meeting.


Meeting  | ____    _______________    ___
         |  _____         ________          __
DNS      |             xxxx
-------------------------------------------------> t
RES.     | ______  ____xxxx_______    ___   __
Sample input (for simplicity, all intervals include the left point and exclude the right point):


Meetings: [(1, 7), (5, 10), (12, 30), (22, 30), (40, 50), (60, 70)]
DNS: (18, 25)
Sample output: [(1, 10), (12, 18), (25, 30), (40, 50), (60, 70)]

"""


def func(meetings, dns):

    if not meetings or not dns:
        return []

    trim = []

    for s, e in meetings:
        if s < dns[0] <= e:
            trim.append([s, min(e, dns[0])])
        elif s <= dns[1] < e:
            trim.append([dns[1], e])
        else:
            trim.append([s, e])

    trim.sort()
    intervals = [trim[0]]

    for t in trim[1:]:
        last = intervals[-1]
        if last[1] >= t[0]:
            last[1] = max(last[1], t[1])
        else:
            intervals.append(t)

    return intervals


print(func([[1, 7], [5, 10], [12, 30], [22, 30], [40, 50], [60, 70]], [18, 25]))

# https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
import heapq


def leastInterval(tasks, n):

    c = Counter(tasks)
    # frequncy of all tasks
    mh = [-v for k, v in c.items()]
    heapq.heapify(mh)
    time = 0
    q = deque()  # pairs of [count, idetime + time_gap]

    while mh or q:

        time += 1
        if mh:
            # adding one because values are -neg and reducing their frequency
            cnt = 1 + heapq.heappop(mh)
            if cnt:
                # count left and time + wait time
                q.append([cnt, time + n])
        # if top value of queue is equals to current time that can allow to proceed again.
        if q and q[0][1] == time:
            heapq.heappush(mh, q.popleft()[0])

    return time


print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 8
print(leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # 6

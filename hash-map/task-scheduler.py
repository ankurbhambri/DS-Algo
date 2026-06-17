# https://leetcode.com/problems/task-scheduler/


import heapq
from collections import Counter, deque
import math


# Heap
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

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


print(Solution().leastInterval(["A", "A", "A", "B", "C", "D"], 2))  # 7
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # 6


# Greedy + Math
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        # 1. Har task ki frequency nikaalein
        count = Counter(tasks)

        # 2. Jo task sabse zyada baar aaya hai uski frequency nikaalein
        max_freq = max(count.values())

        # 3. Pata karein ki aise kitne tasks hain jin ki frequency 'max_freq' ke barabar hai
        # Jaise upar wale example mein A aur B dono ki frequency 3 thi, toh count_max_freq = 2 hoga.
        count_max_freq = sum(1 for freq in count.values() if freq == max_freq)

        # 4. Formula lagayein
        ans = (max_freq - 1) * (n + 1) + count_max_freq

        # Edge Case: Agar tasks itne zyada hain ki khaali slots kam pad gaye aur
        # koi idle time bacha hi nahi, toh answer total number of tasks ke barabar hoga.
        return max(ans, len(tasks))


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 8
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # 6


# Variant: What if we can use multiple CPUs to execute tasks in parallel.

class Solution:
    def minCPUsForBestTime(self, tasks, n):

        total_tasks = len(tasks)

        if total_tasks == 0:
            return 0

        count = Counter(tasks)

        max_freq = max(count.values())

        count_max_freq = sum(1 for freq in count.values() if freq == max_freq)

        # Upper bound logic: Har max_freq task ko unique CPU chahiye parallel mein
        # Lower bound logic: Total tasks ko max_freq rounds mein divide karne ke liye kitne CPUs chahiye
        min_cpus_needed = math.ceil(total_tasks / max_freq)

        # Hamein yeh bhi check karna hoga ki max_freq wale tasks aapas mein collide na karein
        return max(min_cpus_needed, count_max_freq)


# Case 1: Ek hi CPU kaafi tha kyunki slots adjust ho rahe the
print(
    Solution().minCPUsForBestTime(["A", "A", "A", "B", "B", "B"], 2)
)  # Output: 2 (CPU 1: A->B->A, CPU 2: B->A->B)

# Case 2: Agar bohot saare same tasks hain toh zyada CPUs lagenge
print(Solution().minCPUsForBestTime(["A", "A", "A", "A"], 2))  # Output: 1
# Kyunki n = 2 hai, single CPU par: A -> idle -> idle -> A -> idle -> idle -> A -> idle -> idle -> A
# Agar time optimize karna hai bina idle ke, toh har 'A' ko alag CPU chahiye hoga: 4 CPUs!